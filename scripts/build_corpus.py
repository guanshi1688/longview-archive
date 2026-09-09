#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
Build a timestamped, local-only Longview Archive corpus.

Default project layout:

    C:\Users\Admin\Documents\战略\git\
    ├─ longview-archive\
    │  ├─ docs\
    │  ├─ mkdocs.yml
    │  └─ scripts\
    │     └─ build_corpus.py
    └─ index\
       └─ current\
          └─ corpus\
             └─ Longview_Corpus_YYYY-MM-DD_HHMM.md

Corpus inclusion rule:

    mkdocs.yml is the whitelist / catalog.

    ACTIVE NAV ENTRY
        -> PUBLIC
        -> include full Markdown body

    COMMENTED .md ENTRY IN mkdocs.yml
        -> UNPUBLISHED or INTERNAL
        -> include full body only when the file actually exists

    exclude_docs .md ENTRY
        -> INTERNAL
        -> include full body only when the file actually exists

    Markdown file under docs/ that is NOT referenced anywhere above
        -> UNREFERENCED
        -> report path only
        -> DO NOT merge body into Corpus

This means generated bundles such as _bundle.md, *_full.md, 合订本.md, or files
inside _build/ are naturally excluded as long as they are not referenced by
mkdocs.yml. No filename-size or bundle-name heuristic is required.

Design rules:
1. The script itself lives in the Git repository.
2. Generated corpus files live OUTSIDE the Git repository.
3. Every run creates a new timestamped snapshot; no old file is deleted.
4. The complete raw mkdocs.yml is copied near the beginning of the corpus.
5. Active nav entries are treated as PUBLIC.
6. Commented Markdown references are treated as non-public catalog entries.
7. Unreferenced Markdown files are listed for diagnosis but their bodies are not merged.
8. Missing ACTIVE nav files are reported as possible 404/navigation errors.
9. Missing COMMENTED references are reported separately and do not fail the build.
10. The script never modifies Markdown, mkdocs.yml, Git state, or old corpus files.
"""

from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

try:
    import yaml
except ImportError:
    print(
        "ERROR: PyYAML is required. Install it with:\n"
        "    python -m pip install PyYAML",
        file=sys.stderr,
    )
    raise SystemExit(2)


@dataclass
class NavPage:
    title: str
    rel_path: str
    breadcrumb: str
    order: int


@dataclass
class CommentedRef:
    rel_path: str
    title: str
    status: str
    line_no: int


@dataclass
class FileRecord:
    abs_path: Path
    rel_path: str
    title: str
    language: str
    status: str
    section: str
    nav_order: int | None = None
    yaml_line: int | None = None
    note: str = ""


def now_local() -> dt.datetime:
    return dt.datetime.now().astimezone()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def normalize_rel_path(value: str) -> str:
    value = value.strip().strip("'\"").replace("\\", "/")
    while value.startswith("./"):
        value = value[2:]
    return str(PurePosixPath(value))


def first_h1(text: str) -> str | None:
    lines = text.splitlines()
    start = 0

    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                start = i + 1
                break

    for line in lines[start:]:
        m = re.match(r"^\s*#\s+(.+?)\s*$", line)
        if m:
            return m.group(1).strip()
    return None


def infer_language(rel_path: str) -> str:
    p = "/" + rel_path.lower().strip("/") + "/"

    if "/chinese/" in p:
        return "zh"
    if "/english/" in p:
        return "en"

    if rel_path.lower() in {"index.md", "author.md", "copyright.md", "versions.md"}:
        return "en"

    return "unknown"


def safe_repo_relative(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return str(path.resolve())


def separator(char: str = "=", width: int = 96) -> str:
    return char * width


def run_git(repo_root: Path, *args: str) -> str | None:
    try:
        cp = subprocess.run(
            ["git", "-C", str(repo_root), *args],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        return cp.stdout.strip()
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None


def git_metadata(repo_root: Path) -> tuple[str, str]:
    commit = run_git(repo_root, "rev-parse", "--short", "HEAD") or "UNKNOWN"
    status = run_git(repo_root, "status", "--porcelain")
    dirty = "UNKNOWN" if status is None else ("YES" if status else "NO")
    return commit, dirty


def flatten_nav(nav: Any) -> list[NavPage]:
    pages: list[NavPage] = []
    counter = 0

    def walk(node: Any, parents: list[str]) -> None:
        nonlocal counter

        if isinstance(node, str):
            counter += 1
            rel = normalize_rel_path(node)
            title = PurePosixPath(rel).stem
            breadcrumb = " / ".join(parents + [title])
            pages.append(NavPage(title, rel, breadcrumb, counter))
            return

        if isinstance(node, list):
            for item in node:
                walk(item, parents)
            return

        if isinstance(node, dict):
            for key, value in node.items():
                key_str = str(key)

                if isinstance(value, str):
                    counter += 1
                    rel = normalize_rel_path(value)
                    breadcrumb = " / ".join(parents + [key_str])
                    pages.append(NavPage(key_str, rel, breadcrumb, counter))
                else:
                    walk(value, parents + [key_str])

    walk(nav, [])
    return pages


def parse_exclude_patterns(config: dict[str, Any]) -> list[str]:
    raw = config.get("exclude_docs")
    if not raw:
        return []

    if isinstance(raw, str):
        lines = raw.splitlines()
    elif isinstance(raw, list):
        lines = [str(x) for x in raw]
    else:
        lines = [str(raw)]

    patterns: list[str] = []

    for line in lines:
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        patterns.append(normalize_rel_path(s))

    return patterns


def resolve_excluded_markdown(
    docs_dir: Path,
    patterns: list[str],
) -> tuple[list[str], list[str]]:
    existing: set[str] = set()
    missing_exact: list[str] = []

    all_md = [
        p.relative_to(docs_dir).as_posix()
        for p in docs_dir.rglob("*.md")
        if p.is_file()
    ]

    for pattern in patterns:
        if not pattern.lower().endswith(".md"):
            continue

        has_glob = any(ch in pattern for ch in "*?[")

        if has_glob:
            for rel in all_md:
                if fnmatch.fnmatch(rel, pattern):
                    existing.add(rel)
        else:
            abs_path = docs_dir / Path(*PurePosixPath(pattern).parts)
            if abs_path.is_file():
                existing.add(pattern)
            else:
                missing_exact.append(pattern)

    return sorted(existing), missing_exact


MD_PATH_RE = re.compile(r"(?P<path>[^\s:#'\"]+\.md)\b", re.IGNORECASE)


def extract_title_from_commented_line(line: str, rel_path: str) -> str:
    cleaned = re.sub(r"^\s*#+\s*", "", line).strip()
    cleaned = re.sub(r"^-\s*", "", cleaned).strip()

    path_pos = cleaned.find(rel_path)
    if path_pos >= 0:
        prefix = cleaned[:path_pos].rstrip()
        if prefix.endswith(":"):
            prefix = prefix[:-1].rstrip()
        if prefix:
            return prefix

    return PurePosixPath(rel_path).stem


def classify_commented_ref(
    rel_path: str,
    line: str,
    recent_comment_lines: list[str],
) -> str:
    low_path = rel_path.lower()
    context = "\n".join(recent_comment_lines[-12:] + [line]).lower()

    if (
        "internal only" in context
        or "internal" in context
        or "submission" in low_path
        or "reference" in low_path
        or "memo" in low_path
        or "archive-v1-" in low_path
        or PurePosixPath(low_path).name.startswith("90-")
    ):
        return "INTERNAL"

    return "UNPUBLISHED"


def extract_commented_markdown_refs(raw_yaml: str) -> list[CommentedRef]:
    refs: list[CommentedRef] = []
    seen: set[str] = set()
    recent_comment_lines: list[str] = []

    for line_no, line in enumerate(raw_yaml.splitlines(), start=1):
        stripped = line.lstrip()

        if not stripped.startswith("#"):
            recent_comment_lines = []
            continue

        recent_comment_lines.append(stripped)

        m = MD_PATH_RE.search(stripped)
        if not m:
            continue

        rel = normalize_rel_path(m.group("path").rstrip(".,);]"))

        if rel in seen:
            continue
        seen.add(rel)

        refs.append(
            CommentedRef(
                rel_path=rel,
                title=extract_title_from_commented_line(stripped, rel),
                status=classify_commented_ref(rel, stripped, recent_comment_lines),
                line_no=line_no,
            )
        )

    return refs


def build_records(
    docs_dir: Path,
    nav_pages: list[NavPage],
    commented_refs: list[CommentedRef],
    excluded_md_paths: list[str],
):
    nav_by_path: dict[str, NavPage] = {}
    duplicate_nav: list[tuple[NavPage, NavPage]] = []

    for page in nav_pages:
        rel = normalize_rel_path(page.rel_path)
        if rel in nav_by_path:
            duplicate_nav.append((nav_by_path[rel], page))
        else:
            nav_by_path[rel] = page

    records: list[FileRecord] = []
    missing_nav: list[NavPage] = []
    missing_commented: list[CommentedRef] = []
    included_paths: set[str] = set()
    referenced_paths: set[str] = set()

    # ACTIVE NAV -> PUBLIC
    for page in nav_pages:
        rel = normalize_rel_path(page.rel_path)
        referenced_paths.add(rel)

        abs_path = docs_dir / Path(*PurePosixPath(rel).parts)

        if not abs_path.is_file():
            missing_nav.append(page)
            continue

        if rel in included_paths:
            continue

        included_paths.add(rel)
        body = read_text(abs_path)

        records.append(
            FileRecord(
                abs_path=abs_path,
                rel_path=rel,
                title=page.title or first_h1(body) or abs_path.stem,
                language=infer_language(rel),
                status="PUBLIC",
                section=page.breadcrumb,
                nav_order=page.order,
                note="Referenced by active MkDocs nav.",
            )
        )

    # COMMENTED .md -> UNPUBLISHED / INTERNAL
    for ref in commented_refs:
        rel = normalize_rel_path(ref.rel_path)
        referenced_paths.add(rel)

        if rel in included_paths:
            continue

        abs_path = docs_dir / Path(*PurePosixPath(rel).parts)

        if not abs_path.is_file():
            missing_commented.append(ref)
            continue

        included_paths.add(rel)
        body = read_text(abs_path)

        records.append(
            FileRecord(
                abs_path=abs_path,
                rel_path=rel,
                title=ref.title or first_h1(body) or abs_path.stem,
                language=infer_language(rel),
                status=ref.status,
                section=f"COMMENTED YAML / {PurePosixPath(rel).parent.as_posix()}",
                yaml_line=ref.line_no,
                note="Referenced by a commented Markdown entry in mkdocs.yml.",
            )
        )

    # exclude_docs -> INTERNAL
    for rel in excluded_md_paths:
        rel = normalize_rel_path(rel)
        referenced_paths.add(rel)

        if rel in included_paths:
            continue

        abs_path = docs_dir / Path(*PurePosixPath(rel).parts)
        if not abs_path.is_file():
            continue

        included_paths.add(rel)
        body = read_text(abs_path)

        records.append(
            FileRecord(
                abs_path=abs_path,
                rel_path=rel,
                title=first_h1(body) or abs_path.stem,
                language=infer_language(rel),
                status="INTERNAL",
                section="MKDOCS / exclude_docs",
                note="Explicitly referenced by mkdocs.yml exclude_docs.",
            )
        )

    return (
        records,
        missing_nav,
        duplicate_nav,
        missing_commented,
        sorted(referenced_paths),
    )


def find_unreferenced_markdown(
    docs_dir: Path,
    referenced_paths: Iterable[str],
) -> list[str]:
    referenced = {normalize_rel_path(p) for p in referenced_paths}

    all_md = sorted(
        p.relative_to(docs_dir).as_posix()
        for p in docs_dir.rglob("*.md")
        if p.is_file()
    )

    return [rel for rel in all_md if rel not in referenced]


def count_status(records: Iterable[FileRecord], status: str) -> int:
    return sum(1 for r in records if r.status == status)


def write_corpus(
    output_file: Path,
    repo_root: Path,
    docs_dir: Path,
    mkdocs_path: Path,
    raw_yaml: str,
    records: list[FileRecord],
    nav_pages: list[NavPage],
    commented_refs: list[CommentedRef],
    missing_nav: list[NavPage],
    duplicate_nav: list[tuple[NavPage, NavPage]],
    missing_commented: list[CommentedRef],
    missing_excluded: list[str],
    unreferenced_md: list[str],
    git_commit: str,
    git_dirty: str,
    generated_at: dt.datetime,
) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)

    public_count = count_status(records, "PUBLIC")
    unpublished_count = count_status(records, "UNPUBLISHED")
    internal_count = count_status(records, "INTERNAL")

    with output_file.open("w", encoding="utf-8", newline="\n") as out:
        out.write("<<< CORPUS_METADATA >>>\n\n")
        out.write("CORPUS: Longview Archive Full Corpus\n")
        out.write("INCLUSION_MODE: YAML_WHITELIST\n")
        out.write(f"GENERATED_AT: {generated_at.isoformat(timespec='seconds')}\n")
        out.write(f"SOURCE_REPOSITORY: {repo_root}\n")
        out.write(f"SOURCE_MKDOCS: {safe_repo_relative(mkdocs_path, repo_root)}\n")
        out.write(f"SOURCE_DOCS_DIR: {safe_repo_relative(docs_dir, repo_root)}\n")
        out.write(f"SOURCE_GIT_COMMIT: {git_commit}\n")
        out.write(f"SOURCE_GIT_DIRTY: {git_dirty}\n")
        out.write(f"TOTAL_INCLUDED_DOCUMENTS: {len(records)}\n")
        out.write(f"PUBLIC_DOCUMENTS: {public_count}\n")
        out.write(f"UNPUBLISHED_DOCUMENTS: {unpublished_count}\n")
        out.write(f"INTERNAL_DOCUMENTS: {internal_count}\n")
        out.write(f"ACTIVE_NAV_REFERENCES: {len(nav_pages)}\n")
        out.write(f"COMMENTED_MD_REFERENCES: {len(commented_refs)}\n")
        out.write(f"UNREFERENCED_MARKDOWN_FILES: {len(unreferenced_md)}\n")
        out.write(f"MISSING_ACTIVE_NAV_FILES: {len(missing_nav)}\n")
        out.write(f"MISSING_COMMENTED_REFERENCES: {len(missing_commented)}\n")
        out.write(f"MISSING_EXCLUDE_DOC_REFERENCES: {len(missing_excluded)}\n")
        out.write(f"DUPLICATE_ACTIVE_NAV_PATHS: {len(duplicate_nav)}\n\n")
        out.write("<<< CORPUS_METADATA_END >>>\n\n")

        out.write(separator() + "\n")
        out.write("<<< MKDOCS_VALIDATION_BEGIN >>>\n")
        out.write(separator() + "\n\n")

        if not missing_nav:
            out.write("MISSING_ACTIVE_NAV_FILES: 0\n")
            out.write("RESULT: Active MkDocs nav file check OK.\n\n")
        else:
            out.write(f"MISSING_ACTIVE_NAV_FILES: {len(missing_nav)}\n")
            out.write("RESULT: WARNING — active MkDocs nav references missing files.\n")
            out.write("These entries may create broken navigation / 404-like links.\n\n")

            for i, page in enumerate(missing_nav, 1):
                out.write(f"[MISSING ACTIVE {i:03d}]\n")
                out.write(f"TITLE: {page.title}\n")
                out.write(f"PATH: {page.rel_path}\n")
                out.write(f"NAV: {page.breadcrumb}\n")
                out.write("ERROR: FILE NOT FOUND UNDER docs_dir\n\n")

        out.write(f"DUPLICATE_ACTIVE_NAV_PATHS: {len(duplicate_nav)}\n")

        for i, (first, duplicate) in enumerate(duplicate_nav, 1):
            out.write(f"\n[DUPLICATE {i:03d}]\n")
            out.write(f"PATH: {duplicate.rel_path}\n")
            out.write(f"FIRST_NAV: {first.breadcrumb}\n")
            out.write(f"DUPLICATE_NAV: {duplicate.breadcrumb}\n")

        out.write("\n")
        out.write(f"MISSING_COMMENTED_REFERENCES: {len(missing_commented)}\n")

        if missing_commented:
            out.write(
                "NOTE: Commented/planned YAML entries are not public 404 errors.\n"
            )
            for i, ref in enumerate(missing_commented, 1):
                out.write(f"\n[MISSING COMMENTED {i:03d}]\n")
                out.write(f"PATH: {ref.rel_path}\n")
                out.write(f"STATUS: {ref.status}\n")
                out.write(f"YAML_LINE: {ref.line_no}\n")

        out.write("\n")
        out.write(f"MISSING_EXCLUDE_DOC_REFERENCES: {len(missing_excluded)}\n")
        for rel in missing_excluded:
            out.write(f"- {rel}\n")

        out.write("\n" + separator() + "\n")
        out.write("<<< MKDOCS_VALIDATION_END >>>\n")
        out.write(separator() + "\n\n")

        out.write(separator() + "\n")
        out.write("<<< MKDOCS_YAML_BEGIN >>>\n")
        out.write(separator() + "\n\n")
        out.write(raw_yaml)

        if raw_yaml and not raw_yaml.endswith("\n"):
            out.write("\n")

        out.write("\n")
        out.write(separator() + "\n")
        out.write("<<< MKDOCS_YAML_END >>>\n")
        out.write(separator() + "\n\n")

        # Diagnostic only. No unreferenced file body is merged.
        out.write(separator() + "\n")
        out.write("<<< UNREFERENCED_MARKDOWN_FILES_BEGIN >>>\n")
        out.write(separator() + "\n\n")
        out.write(f"COUNT: {len(unreferenced_md)}\n")
        out.write("CONTENT_INCLUDED: NO\n")
        out.write(
            "RULE: Exists under docs/ but is not referenced by active nav, "
            "commented .md entries, or exclude_docs in mkdocs.yml.\n\n"
        )

        for rel in unreferenced_md:
            out.write(f"- {rel}\n")

        out.write("\n")
        out.write(separator() + "\n")
        out.write("<<< UNREFERENCED_MARKDOWN_FILES_END >>>\n")
        out.write(separator() + "\n\n")

        if missing_nav:
            out.write(separator() + "\n")
            out.write("<<< MISSING_ACTIVE_NAV_FILES_BEGIN >>>\n")
            out.write(separator() + "\n\n")

            for page in missing_nav:
                out.write(separator("-") + "\n")
                out.write("<<< FILE_MISSING >>>\n\n")
                out.write(f"TITLE: {page.title}\n")
                out.write(f"PATH: {page.rel_path}\n")
                out.write("STATUS: MISSING\n")
                out.write(f"SECTION: {page.breadcrumb}\n")
                out.write("ERROR: Referenced by active mkdocs.yml nav but file was not found.\n")
                out.write(separator("-") + "\n\n")

            out.write(separator() + "\n")
            out.write("<<< MISSING_ACTIVE_NAV_FILES_END >>>\n")
            out.write(separator() + "\n\n")

        current_section: str | None = None

        for record in records:
            if record.section != current_section:
                if current_section is not None:
                    out.write(separator() + "\n")
                    out.write("<<< SECTION_END >>>\n")
                    out.write(f"NAME: {current_section}\n")
                    out.write(separator() + "\n\n")

                current_section = record.section
                out.write(separator() + "\n")
                out.write("<<< SECTION_BEGIN >>>\n")
                out.write(f"NAME: {current_section}\n")
                out.write(separator() + "\n\n")

            body = read_text(record.abs_path)

            out.write(separator("-") + "\n")
            out.write("<<< FILE_BEGIN >>>\n\n")
            out.write(f"TITLE: {record.title}\n")
            out.write(f"PATH: {record.rel_path}\n")
            out.write(f"LANGUAGE: {record.language}\n")
            out.write(f"STATUS: {record.status}\n")
            out.write(f"SECTION: {record.section}\n")

            if record.nav_order is not None:
                out.write(f"NAV_ORDER: {record.nav_order}\n")

            if record.yaml_line is not None:
                out.write(f"YAML_LINE: {record.yaml_line}\n")

            if record.note:
                out.write(f"NOTE: {record.note}\n")

            out.write("\n<<< CONTENT_BEGIN >>>\n")
            out.write(separator("-") + "\n\n")
            out.write(body)

            if body and not body.endswith("\n"):
                out.write("\n")

            out.write("\n")
            out.write(separator("-") + "\n")
            out.write("<<< CONTENT_END >>>\n\n")
            out.write("<<< FILE_END >>>\n")
            out.write(f"PATH: {record.rel_path}\n")
            out.write(separator("-") + "\n\n")

        if current_section is not None:
            out.write(separator() + "\n")
            out.write("<<< SECTION_END >>>\n")
            out.write(f"NAME: {current_section}\n")
            out.write(separator() + "\n\n")

        out.write("<<< CORPUS_END >>>\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a timestamped YAML-driven Longview Archive corpus."
    )

    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Repository root. Default: parent of this script's scripts/ directory.",
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory. Default: <repo-parent>/index/current/corpus",
    )

    parser.add_argument(
        "--mkdocs",
        type=Path,
        default=None,
        help="mkdocs.yml path. Default: <repo-root>/mkdocs.yml",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    script_dir = Path(__file__).resolve().parent
    repo_root = (args.repo_root or script_dir.parent).resolve()
    mkdocs_path = (args.mkdocs or (repo_root / "mkdocs.yml")).resolve()

    if not mkdocs_path.is_file():
        print(f"ERROR: mkdocs.yml not found: {mkdocs_path}", file=sys.stderr)
        return 2

    raw_yaml = read_text(mkdocs_path)

    try:
        config = yaml.safe_load(raw_yaml) or {}
    except yaml.YAMLError as exc:
        print(f"ERROR: mkdocs.yml cannot be parsed as YAML:\n{exc}", file=sys.stderr)
        return 2

    if not isinstance(config, dict):
        print("ERROR: mkdocs.yml root must be a mapping/object.", file=sys.stderr)
        return 2

    docs_dir = (repo_root / str(config.get("docs_dir", "docs"))).resolve()

    if not docs_dir.is_dir():
        print(f"ERROR: docs_dir does not exist: {docs_dir}", file=sys.stderr)
        return 2

    nav_pages = flatten_nav(config.get("nav", []))
    commented_refs = extract_commented_markdown_refs(raw_yaml)

    exclude_patterns = parse_exclude_patterns(config)
    excluded_md_paths, missing_excluded = resolve_excluded_markdown(
        docs_dir,
        exclude_patterns,
    )

    (
        records,
        missing_nav,
        duplicate_nav,
        missing_commented,
        referenced_paths,
    ) = build_records(
        docs_dir,
        nav_pages,
        commented_refs,
        excluded_md_paths,
    )

    referenced_paths = sorted(set(referenced_paths) | set(excluded_md_paths))
    unreferenced_md = find_unreferenced_markdown(docs_dir, referenced_paths)

    generated_at = now_local()
    stamp = generated_at.strftime("%Y-%m-%d_%H%M")

    output_dir = (
        args.output_dir.resolve()
        if args.output_dir
        else (repo_root.parent / "index" / "current" / "corpus").resolve()
    )

    output_file = output_dir / f"Longview_Corpus_{stamp}.md"

    if output_file.exists():
        stamp = generated_at.strftime("%Y-%m-%d_%H%M%S")
        output_file = output_dir / f"Longview_Corpus_{stamp}.md"

    git_commit, git_dirty = git_metadata(repo_root)

    write_corpus(
        output_file=output_file,
        repo_root=repo_root,
        docs_dir=docs_dir,
        mkdocs_path=mkdocs_path,
        raw_yaml=raw_yaml,
        records=records,
        nav_pages=nav_pages,
        commented_refs=commented_refs,
        missing_nav=missing_nav,
        duplicate_nav=duplicate_nav,
        missing_commented=missing_commented,
        missing_excluded=missing_excluded,
        unreferenced_md=unreferenced_md,
        git_commit=git_commit,
        git_dirty=git_dirty,
        generated_at=generated_at,
    )

    print()
    print("Longview corpus build complete.")
    print(f"Repository                 : {repo_root}")
    print(f"Docs                       : {docs_dir}")
    print(f"Output                     : {output_file}")
    print()
    print(f"Included documents         : {len(records)}")
    print(f"Public                     : {count_status(records, 'PUBLIC')}")
    print(f"Unpublished                : {count_status(records, 'UNPUBLISHED')}")
    print(f"Internal                   : {count_status(records, 'INTERNAL')}")
    print(f"Active nav references      : {len(nav_pages)}")
    print(f"Commented .md references   : {len(commented_refs)}")
    print(f"Unreferenced .md files     : {len(unreferenced_md)}")
    print(f"Missing active nav files   : {len(missing_nav)}")
    print(f"Missing commented refs     : {len(missing_commented)}")
    print(f"Duplicate nav paths        : {len(duplicate_nav)}")
    print()

    if missing_nav:
        print("WARNING: Missing files referenced by active mkdocs.yml nav:")
        for page in missing_nav:
            print(f"  - {page.rel_path}  [{page.breadcrumb}]")
        print()
        print("The corpus was still generated. Missing active entries are recorded inside it.")
        return 1

    print("MkDocs active-nav file check: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
