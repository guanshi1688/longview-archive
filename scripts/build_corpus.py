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

Design rules:
1. The script itself lives in the Git repository.
2. Generated corpus files live OUTSIDE the Git repository.
3. Every run creates a new timestamped snapshot; no old file is deleted.
4. mkdocs.yml is copied verbatim to the beginning of the corpus.
5. Active mkdocs nav entries are treated as PUBLIC.
6. Every Markdown file under docs/ is included, including files not in active nav.
7. Active nav entries that point to missing files are reported explicitly, so
   possible 404/navigation problems are visible inside the corpus and on stdout.
8. The script never modifies source Markdown, mkdocs.yml, Git state, or old corpus files.
"""

from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import os
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


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class NavPage:
    title: str
    rel_path: str
    breadcrumb: str
    order: int


@dataclass
class FileRecord:
    abs_path: Path
    rel_path: str
    title: str
    language: str
    status: str
    section: str
    nav_order: int | None = None
    note: str = ""


# ---------------------------------------------------------------------------
# Basic helpers
# ---------------------------------------------------------------------------

def now_local() -> dt.datetime:
    return dt.datetime.now().astimezone()


def read_text(path: Path) -> str:
    """Read UTF-8 text while tolerating a UTF-8 BOM."""
    return path.read_text(encoding="utf-8-sig")


def normalize_rel_path(value: str) -> str:
    """
    Normalize an MkDocs/doc relative path to forward-slash form.
    MkDocs nav paths are relative to docs_dir.
    """
    value = value.strip().replace("\\", "/")
    while value.startswith("./"):
        value = value[2:]
    return str(PurePosixPath(value))


def first_h1(text: str) -> str | None:
    """Return the first Markdown H1 outside the simplest front-matter case."""
    lines = text.splitlines()
    start = 0

    # Skip YAML front matter if present.
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

    # Root/public administrative pages are usually English in this project.
    if rel_path.lower() in {"index.md", "author.md", "copyright.md", "versions.md"}:
        return "en"

    return "unknown"


def safe_repo_relative(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return str(path.resolve())


# ---------------------------------------------------------------------------
# Git metadata
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# MkDocs parsing
# ---------------------------------------------------------------------------

def flatten_nav(nav: Any) -> list[NavPage]:
    """
    Flatten MkDocs nav while preserving order and breadcrumb hierarchy.

    Supported common forms:
      - Home: index.md
      - Section:
          - Page: path.md
          - Subsection:
              - Page: path.md
      - path.md
    """
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
            return

        # Unknown nav nodes are ignored rather than crashing the build.

    walk(nav, [])
    return pages


def parse_exclude_patterns(config: dict[str, Any]) -> list[str]:
    """
    Parse simple exclude_docs entries. MkDocs accepts multiline patterns.
    We keep this intentionally conservative.
    """
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


def is_excluded(rel_path: str, patterns: list[str]) -> bool:
    rel = normalize_rel_path(rel_path)
    for pat in patterns:
        # Support both simple exact names and glob-like patterns.
        if rel == pat or fnmatch.fnmatch(rel, pat):
            return True
    return False


# ---------------------------------------------------------------------------
# Status classification
# ---------------------------------------------------------------------------

INTERNAL_MARKERS = {
    "submission",
    "submission-rewrite",
    "submission_rewrite",
    "memo",
    "references",
    "reference",
    "private",
    "internal",
    "draft",
}

UNPUBLISHED_MARKERS = {
    "structural-algorithm",
}


def classify_unlisted(rel_path: str, excluded: bool) -> tuple[str, str]:
    """
    Classify Markdown files that are NOT present in active nav.

    Important:
    - Active nav always wins and is PUBLIC.
    - Non-nav files are never silently dropped.
    """
    low = rel_path.lower()
    parts = {p.lower() for p in PurePosixPath(low).parts}
    name = PurePosixPath(low).name

    if excluded:
        return "INTERNAL", "Excluded from MkDocs by exclude_docs."

    if (
        name.startswith("90-")
        or any(marker in low for marker in INTERNAL_MARKERS)
        or "archive-v1-" in low
    ):
        return "INTERNAL", "Not in active nav; classified by internal-file rule."

    if any(marker in parts or marker in low for marker in UNPUBLISHED_MARKERS):
        return "UNPUBLISHED", "Not in active nav; classified as planned/unpublished theory."

    # For this corpus, an existing essay not present in active nav is still useful
    # theory material. Mark it UNPUBLISHED rather than dropping it.
    return "UNPUBLISHED", "Existing Markdown file not present in active MkDocs nav."


# ---------------------------------------------------------------------------
# Corpus construction
# ---------------------------------------------------------------------------

def build_records(
    docs_dir: Path,
    nav_pages: list[NavPage],
    exclude_patterns: list[str],
) -> tuple[list[FileRecord], list[NavPage], list[tuple[NavPage, NavPage]]]:
    """
    Returns:
      records          all existing Markdown docs (public first, then unlisted)
      missing_nav      active nav references whose files do not exist
      duplicate_nav    repeated active nav path references
    """
    nav_by_path: dict[str, NavPage] = {}
    duplicate_nav: list[tuple[NavPage, NavPage]] = []

    for page in nav_pages:
        rel = normalize_rel_path(page.rel_path)
        if rel in nav_by_path:
            duplicate_nav.append((nav_by_path[rel], page))
        else:
            nav_by_path[rel] = page

    missing_nav: list[NavPage] = []
    public_records: list[FileRecord] = []
    seen_existing: set[str] = set()

    # Active nav order first.
    for page in nav_pages:
        rel = normalize_rel_path(page.rel_path)
        abs_path = docs_dir / Path(*PurePosixPath(rel).parts)

        if not abs_path.is_file():
            missing_nav.append(page)
            continue

        if rel in seen_existing:
            continue
        seen_existing.add(rel)

        text = read_text(abs_path)
        title = page.title or first_h1(text) or abs_path.stem
        public_records.append(
            FileRecord(
                abs_path=abs_path,
                rel_path=rel,
                title=title,
                language=infer_language(rel),
                status="PUBLIC",
                section=page.breadcrumb,
                nav_order=page.order,
                note="Referenced by active MkDocs nav.",
            )
        )

    # Then every other Markdown file under docs.
    extra_records: list[FileRecord] = []
    if docs_dir.is_dir():
        all_md = sorted(
            (p for p in docs_dir.rglob("*.md") if p.is_file()),
            key=lambda p: p.relative_to(docs_dir).as_posix().lower(),
        )
    else:
        all_md = []

    for abs_path in all_md:
        rel = abs_path.relative_to(docs_dir).as_posix()
        if rel in seen_existing:
            continue

        text = read_text(abs_path)
        title = first_h1(text) or abs_path.stem
        excluded = is_excluded(rel, exclude_patterns)
        status, note = classify_unlisted(rel, excluded)

        parent = PurePosixPath(rel).parent.as_posix()
        section = f"UNLISTED / {parent}" if parent != "." else "UNLISTED / ROOT"

        extra_records.append(
            FileRecord(
                abs_path=abs_path,
                rel_path=rel,
                title=title,
                language=infer_language(rel),
                status=status,
                section=section,
                nav_order=None,
                note=note,
            )
        )

    return public_records + extra_records, missing_nav, duplicate_nav


def count_status(records: Iterable[FileRecord], status: str) -> int:
    return sum(1 for r in records if r.status == status)


def separator(char: str = "=", width: int = 96) -> str:
    return char * width


def write_corpus(
    output_file: Path,
    repo_root: Path,
    docs_dir: Path,
    mkdocs_path: Path,
    raw_yaml: str,
    records: list[FileRecord],
    nav_pages: list[NavPage],
    missing_nav: list[NavPage],
    duplicate_nav: list[tuple[NavPage, NavPage]],
    git_commit: str,
    git_dirty: str,
    generated_at: dt.datetime,
) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)

    public_count = count_status(records, "PUBLIC")
    unpublished_count = count_status(records, "UNPUBLISHED")
    internal_count = count_status(records, "INTERNAL")
    unclassified_count = count_status(records, "UNCLASSIFIED")
    total_existing = len(records)

    with output_file.open("w", encoding="utf-8", newline="\n") as out:
        # -------------------------------------------------------------------
        # Metadata
        # -------------------------------------------------------------------
        out.write("<<< CORPUS_METADATA >>>\n\n")
        out.write("CORPUS: Longview Archive Full Corpus\n")
        out.write(f"GENERATED_AT: {generated_at.isoformat(timespec='seconds')}\n")
        out.write(f"SOURCE_REPOSITORY: {repo_root}\n")
        out.write(f"SOURCE_MKDOCS: {safe_repo_relative(mkdocs_path, repo_root)}\n")
        out.write(f"SOURCE_DOCS_DIR: {safe_repo_relative(docs_dir, repo_root)}\n")
        out.write(f"SOURCE_GIT_COMMIT: {git_commit}\n")
        out.write(f"SOURCE_GIT_DIRTY: {git_dirty}\n")
        out.write(f"TOTAL_EXISTING_DOCUMENTS: {total_existing}\n")
        out.write(f"PUBLIC_DOCUMENTS: {public_count}\n")
        out.write(f"UNPUBLISHED_DOCUMENTS: {unpublished_count}\n")
        out.write(f"INTERNAL_DOCUMENTS: {internal_count}\n")
        out.write(f"UNCLASSIFIED_DOCUMENTS: {unclassified_count}\n")
        out.write(f"ACTIVE_NAV_REFERENCES: {len(nav_pages)}\n")
        out.write(f"MISSING_ACTIVE_NAV_FILES: {len(missing_nav)}\n")
        out.write(f"DUPLICATE_ACTIVE_NAV_PATHS: {len(duplicate_nav)}\n\n")
        out.write("<<< CORPUS_METADATA_END >>>\n\n")

        # -------------------------------------------------------------------
        # MkDocs validation
        # -------------------------------------------------------------------
        out.write(separator() + "\n")
        out.write("<<< MKDOCS_VALIDATION_BEGIN >>>\n")
        out.write(separator() + "\n\n")

        if not missing_nav:
            out.write("MISSING_ACTIVE_NAV_FILES: 0\n")
            out.write("RESULT: No missing file was found among active MkDocs nav references.\n\n")
        else:
            out.write(f"MISSING_ACTIVE_NAV_FILES: {len(missing_nav)}\n")
            out.write("RESULT: WARNING — active MkDocs nav references missing files.\n")
            out.write("These entries may create broken navigation / 404-like user-facing links.\n\n")
            for i, page in enumerate(missing_nav, 1):
                out.write(f"[MISSING {i:03d}]\n")
                out.write(f"TITLE: {page.title}\n")
                out.write(f"PATH: {page.rel_path}\n")
                out.write(f"NAV: {page.breadcrumb}\n")
                out.write("ERROR: FILE NOT FOUND UNDER docs_dir\n\n")

        if duplicate_nav:
            out.write(f"DUPLICATE_ACTIVE_NAV_PATHS: {len(duplicate_nav)}\n\n")
            for i, (first, duplicate) in enumerate(duplicate_nav, 1):
                out.write(f"[DUPLICATE {i:03d}]\n")
                out.write(f"PATH: {duplicate.rel_path}\n")
                out.write(f"FIRST_NAV: {first.breadcrumb}\n")
                out.write(f"DUPLICATE_NAV: {duplicate.breadcrumb}\n\n")
        else:
            out.write("DUPLICATE_ACTIVE_NAV_PATHS: 0\n\n")

        out.write(separator() + "\n")
        out.write("<<< MKDOCS_VALIDATION_END >>>\n")
        out.write(separator() + "\n\n")

        # -------------------------------------------------------------------
        # Full raw mkdocs.yml
        # -------------------------------------------------------------------
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

        # -------------------------------------------------------------------
        # Missing-file placeholders inside the corpus body as well
        # -------------------------------------------------------------------
        if missing_nav:
            out.write(separator("=") + "\n")
            out.write("<<< MISSING_NAV_FILES_BEGIN >>>\n")
            out.write(separator("=") + "\n\n")
            for page in missing_nav:
                out.write(separator("-") + "\n")
                out.write("<<< FILE_MISSING >>>\n\n")
                out.write(f"TITLE: {page.title}\n")
                out.write(f"PATH: {page.rel_path}\n")
                out.write("STATUS: MISSING\n")
                out.write(f"SECTION: {page.breadcrumb}\n")
                out.write("ERROR: Referenced by active mkdocs.yml nav but file was not found.\n")
                out.write(separator("-") + "\n\n")
            out.write(separator("=") + "\n")
            out.write("<<< MISSING_NAV_FILES_END >>>\n")
            out.write(separator("=") + "\n\n")

        # -------------------------------------------------------------------
        # Existing Markdown content
        # -------------------------------------------------------------------
        current_section: str | None = None

        for record in records:
            if record.section != current_section:
                if current_section is not None:
                    out.write(separator("=") + "\n")
                    out.write("<<< SECTION_END >>>\n")
                    out.write(f"NAME: {current_section}\n")
                    out.write(separator("=") + "\n\n")

                current_section = record.section
                out.write(separator("=") + "\n")
                out.write("<<< SECTION_BEGIN >>>\n")
                out.write(f"NAME: {current_section}\n")
                out.write(separator("=") + "\n\n")

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
            out.write(separator("=") + "\n")
            out.write("<<< SECTION_END >>>\n")
            out.write(f"NAME: {current_section}\n")
            out.write(separator("=") + "\n\n")

        out.write("<<< CORPUS_END >>>\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a timestamped Longview Archive full corpus."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help=(
            "Repository root. Default: parent of the scripts directory "
            "containing this file."
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=(
            "Output directory. Default: <repo-parent>/index/current/corpus"
        ),
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

    docs_dir_value = str(config.get("docs_dir", "docs"))
    docs_dir = (repo_root / docs_dir_value).resolve()

    if not docs_dir.is_dir():
        print(f"ERROR: docs_dir does not exist: {docs_dir}", file=sys.stderr)
        return 2

    nav = config.get("nav", [])
    nav_pages = flatten_nav(nav)
    exclude_patterns = parse_exclude_patterns(config)

    records, missing_nav, duplicate_nav = build_records(
        docs_dir=docs_dir,
        nav_pages=nav_pages,
        exclude_patterns=exclude_patterns,
    )

    generated_at = now_local()
    stamp = generated_at.strftime("%Y-%m-%d_%H%M")

    output_dir = (
        args.output_dir.resolve()
        if args.output_dir
        else (repo_root.parent / "index" / "current" / "corpus").resolve()
    )
    output_file = output_dir / f"Longview_Corpus_{stamp}.md"

    # Extra safety: do not overwrite a corpus if two runs happen in the same minute.
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
        missing_nav=missing_nav,
        duplicate_nav=duplicate_nav,
        git_commit=git_commit,
        git_dirty=git_dirty,
        generated_at=generated_at,
    )

    print()
    print("Longview corpus build complete.")
    print(f"Repository : {repo_root}")
    print(f"Docs       : {docs_dir}")
    print(f"Output     : {output_file}")
    print()
    print(f"Existing documents      : {len(records)}")
    print(f"Public                    : {count_status(records, 'PUBLIC')}")
    print(f"Unpublished               : {count_status(records, 'UNPUBLISHED')}")
    print(f"Internal                  : {count_status(records, 'INTERNAL')}")
    print(f"Unclassified              : {count_status(records, 'UNCLASSIFIED')}")
    print(f"Active nav references     : {len(nav_pages)}")
    print(f"Missing active nav files  : {len(missing_nav)}")
    print(f"Duplicate nav paths       : {len(duplicate_nav)}")
    print()

    if missing_nav:
        print("WARNING: Missing files referenced by active mkdocs.yml nav:")
        for page in missing_nav:
            print(f"  - {page.rel_path}  [{page.breadcrumb}]")
        print()
        print("The corpus was still generated. Missing entries are recorded inside it.")
        return 1

    print("MkDocs nav file check: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
