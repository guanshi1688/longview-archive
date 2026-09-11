#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
Build an AI-friendly, timestamped, local-only Longview Archive corpus.

Default layout:

    <git-root>/
    ├─ longview-archive/
    │  ├─ docs/
    │  │  └─ memo/
    │  │     ├─ theory-map.md
    │  │     └─ file_map.md
    │  ├─ mkdocs.yml
    │  └─ scripts/
    │     └─ build_corpus.py
    └─ index/
       ├─ structural-algorithm/
       │  ├─ chinese/
       │  └─ english/
       ├─ publish/
       │  ├─ question-pool.md
       │  ├─ short-essay-manifest.md
       │  └─ articles/                 # optional; future LV-xxxx working essays
       └─ current/
          └─ corpus/
             └─ Longview_Corpus_YYYY-MM-DD_HHMM.md

The corpus has five source classes:

1. ROUTING DOCUMENTS
   - docs/memo/theory-map.md
   - docs/memo/file_map.md
   These are emitted first because they tell an AI how to interpret the rest.

2. CANONICAL UNPUBLISHED STRUCTURAL THEORY
   - <git-root>/index/structural-algorithm/chinese/*.md
   - <git-root>/index/structural-algorithm/english/*.md
   This material is physically outside the public site repository and is merged
   directly by this script.

3. PUBLIC / CATALOGUED WEBSITE MATERIAL
   - active mkdocs.yml nav -> PUBLIC
   - existing commented .md entry -> UNPUBLISHED / INTERNAL
   - existing exclude_docs .md entry -> INTERNAL

4. WORKING SHORT-ESSAY / PUBLICATION WORKSPACE
   - <git-root>/index/publish/question-pool.md
   - <git-root>/index/publish/short-essay-manifest.md
   - optional additional Markdown under <git-root>/index/publish/
   These files are working registries / derived outputs. They do not outrank theory-map
   or canonical mother text.

5. DIAGNOSTICS / PUBLICATION ROADMAP
   - commented Structural Algorithm paths in mkdocs.yml are treated as RESERVED
     FUTURE NAV PATHS when they do not yet exist under docs/. They are not errors.
   - unreferenced docs Markdown is listed only; its body is not merged.
   - raw mkdocs.yml is copied at the END, not the beginning, so machine readers
     encounter semantic authority before repository diagnostics.

AI-oriented authority order:

    theory-map
      -> foundational Structural Algorithm
      -> structural bridge essays
      -> public canonical archive
      -> auxiliary unpublished/internal material
      -> diagnostics and raw mkdocs.yml

Conflict rules:
- Theory hierarchy / article placement: memo/theory-map.md wins.
- Repository paths / publication state: memo/file_map.md wins.
- A concrete theoretical claim: the corresponding canonical mother text wins.
- Commented Structural Algorithm entries in mkdocs.yml are a future publication
  manifest, not the current physical source of the unpublished mother text.

The script never modifies source Markdown, mkdocs.yml, Git state, or old corpus files.
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
from typing import Any, Iterable, Sequence

try:
    import yaml
except ImportError:
    print(
        "ERROR: PyYAML is required. Install it with:\n"
        "    python -m pip install PyYAML",
        file=sys.stderr,
    )
    raise SystemExit(2)


ROUTING_DOCUMENTS: tuple[str, ...] = (
    "memo/theory-map.md",
    "memo/file_map.md",
)

RESERVED_FUTURE_PREFIXES: tuple[str, ...] = (
    "essays/english/structural-algorithm/",
    "essays/chinese/structural-algorithm/",
)

PUBLISH_REGISTRY_FILES: tuple[str, ...] = (
    "question-pool.md",
    "short-essay-manifest.md",
)


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
    source_kind: str
    authority: str
    role: str
    nav_order: int | None = None
    yaml_line: int | None = None
    note: str = ""


# -----------------------------------------------------------------------------
# Basic helpers
# -----------------------------------------------------------------------------

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

    if rel_path.lower() in {
        "index.md",
        "author.md",
        "copyright.md",
        "versions.md",
        "memo/file_map.md",
    }:
        return "en"

    if rel_path.lower() == "memo/theory-map.md":
        return "zh"

    return "unknown"


def safe_repo_relative(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return str(path.resolve())


def separator(char: str = "=", width: int = 96) -> str:
    return char * width


def natural_key(text: str) -> tuple[Any, ...]:
    parts = re.split(r"(\d+)", text.casefold())
    key: list[Any] = []
    for part in parts:
        if part.isdigit():
            key.append(int(part))
        else:
            key.append(part)
    return tuple(key)


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


# -----------------------------------------------------------------------------
# mkdocs parsing
# -----------------------------------------------------------------------------

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

    return sorted(existing, key=natural_key), sorted(missing_exact, key=natural_key)


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


def is_reserved_future_nav(rel_path: str) -> bool:
    low = normalize_rel_path(rel_path).lower()
    return any(low.startswith(prefix) for prefix in RESERVED_FUTURE_PREFIXES)


# -----------------------------------------------------------------------------
# Website records
# -----------------------------------------------------------------------------

def build_docs_records(
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
    reserved_future: list[CommentedRef] = []
    included_paths: set[str] = set()
    referenced_paths: set[str] = set()

    # ACTIVE NAV -> PUBLIC CANONICAL
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
                source_kind="WEBSITE_DOCS",
                authority="PUBLIC_CANONICAL",
                role="PUBLIC_ARCHIVE",
                nav_order=page.order,
                note="Referenced by active MkDocs nav.",
            )
        )

    # COMMENTED .md -> existing body, or reserved/missing reference
    for ref in commented_refs:
        rel = normalize_rel_path(ref.rel_path)
        referenced_paths.add(rel)

        if rel in included_paths:
            continue

        abs_path = docs_dir / Path(*PurePosixPath(rel).parts)
        if not abs_path.is_file():
            if is_reserved_future_nav(rel):
                reserved_future.append(ref)
            else:
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
                source_kind="WEBSITE_DOCS",
                authority="WORKING_CATALOGUED",
                role="COMMENTED_CATALOGUE",
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
        role = "ROUTING_DOCUMENT" if rel in ROUTING_DOCUMENTS else "INTERNAL_DOC"
        authority = "ROUTING_AUTHORITY" if role == "ROUTING_DOCUMENT" else "INTERNAL_REFERENCE"
        records.append(
            FileRecord(
                abs_path=abs_path,
                rel_path=rel,
                title=first_h1(body) or abs_path.stem,
                language=infer_language(rel),
                status="INTERNAL",
                section="MKDOCS / exclude_docs",
                source_kind="WEBSITE_DOCS",
                authority=authority,
                role=role,
                note="Explicitly referenced by mkdocs.yml exclude_docs.",
            )
        )

    return (
        records,
        missing_nav,
        duplicate_nav,
        missing_commented,
        reserved_future,
        sorted(referenced_paths, key=natural_key),
    )


def ensure_routing_documents(
    docs_dir: Path,
    records: list[FileRecord],
    referenced_paths: set[str],
) -> tuple[list[str], list[str]]:
    """Make routing docs impossible to lose silently.

    If a routing file exists physically but was not catalogued in mkdocs.yml,
    include it directly and report it as a catalog warning. This keeps a corpus
    machine-readable even after a temporary YAML mistake.
    """
    by_path = {r.rel_path: r for r in records}
    missing: list[str] = []
    uncatalogued: list[str] = []

    for rel in ROUTING_DOCUMENTS:
        abs_path = docs_dir / Path(*PurePosixPath(rel).parts)
        if not abs_path.is_file():
            missing.append(rel)
            continue

        referenced_paths.add(rel)
        if rel in by_path:
            r = by_path[rel]
            r.role = "ROUTING_DOCUMENT"
            r.authority = "ROUTING_AUTHORITY"
            r.source_kind = "WEBSITE_DOCS"
            continue

        body = read_text(abs_path)
        records.append(
            FileRecord(
                abs_path=abs_path,
                rel_path=rel,
                title=first_h1(body) or abs_path.stem,
                language=infer_language(rel),
                status="INTERNAL",
                section="DIRECT ROUTING INCLUDE",
                source_kind="WEBSITE_DOCS",
                authority="ROUTING_AUTHORITY",
                role="ROUTING_DOCUMENT",
                note=(
                    "Routing file was included directly because it exists physically "
                    "but is not catalogued by mkdocs.yml. Add it to exclude_docs."
                ),
            )
        )
        uncatalogued.append(rel)

    return missing, uncatalogued


def find_unreferenced_markdown(
    docs_dir: Path,
    referenced_paths: Iterable[str],
) -> list[str]:
    referenced = {normalize_rel_path(p) for p in referenced_paths}
    all_md = sorted(
        (
            p.relative_to(docs_dir).as_posix()
            for p in docs_dir.rglob("*.md")
            if p.is_file()
        ),
        key=natural_key,
    )
    return [rel for rel in all_md if rel not in referenced]


# -----------------------------------------------------------------------------
# External canonical Structural Algorithm
# -----------------------------------------------------------------------------

def classify_structural_role(path: Path) -> tuple[str, str, str]:
    """Return (role, status, authority)."""
    name = path.name.casefold()

    is_bridge = (
        "causal-line-from-geography-to-consumption" in name
        or "geography-to-consumption" in name
        or ("地理" in path.name and "消费" in path.name)
    )
    if is_bridge:
        return "STRUCTURAL_BRIDGE", "CANONICAL_UNPUBLISHED", "DERIVED_CANONICAL"

    if (
        name == "readme.md"
        or "submission" in name
        or "adaptation-memorandum" in name
        or "nav-snippet" in name
    ):
        return "STRUCTURAL_AUXILIARY", "INTERNAL", "NON_CANONICAL_REFERENCE"

    return "STRUCTURAL_CORE", "CANONICAL_UNPUBLISHED", "FOUNDATIONAL_CANONICAL"


def scan_structural_algorithm(structural_root: Path) -> tuple[list[FileRecord], list[str]]:
    records: list[FileRecord] = []
    warnings: list[str] = []

    if not structural_root.is_dir():
        warnings.append(f"Structural Algorithm root not found: {structural_root}")
        return records, warnings

    language_dirs = (
        ("chinese", "zh"),
        ("english", "en"),
    )

    for dirname, language in language_dirs:
        lang_dir = structural_root / dirname
        if not lang_dir.is_dir():
            warnings.append(f"Structural Algorithm language directory not found: {lang_dir}")
            continue

        files = sorted(
            (p for p in lang_dir.rglob("*.md") if p.is_file()),
            key=lambda p: natural_key(p.relative_to(lang_dir).as_posix()),
        )

        for path in files:
            role, status, authority = classify_structural_role(path)
            body = read_text(path)
            inner_rel = path.relative_to(lang_dir).as_posix()
            rel_path = f"index/structural-algorithm/{dirname}/{inner_rel}"

            if role == "STRUCTURAL_CORE":
                section = f"FOUNDATIONAL THEORY / Structural Algorithm / {dirname}"
            elif role == "STRUCTURAL_BRIDGE":
                section = f"STRUCTURAL BRIDGE / {dirname}"
            else:
                section = f"STRUCTURAL AUXILIARY / {dirname}"

            records.append(
                FileRecord(
                    abs_path=path,
                    rel_path=rel_path,
                    title=first_h1(body) or path.stem,
                    language=language,
                    status=status,
                    section=section,
                    source_kind="EXTERNAL_INDEX",
                    authority=authority,
                    role=role,
                    note="Physical source: sibling index/structural-algorithm tree; not served by MkDocs.",
                )
            )

    return records, warnings



# -----------------------------------------------------------------------------
# Working short-essay / publication workspace
# -----------------------------------------------------------------------------

def scan_publish_workspace(publish_root: Path) -> tuple[list[FileRecord], list[str]]:
    """Scan the sibling index/publish workspace.

    Registry files are control-plane working state. Other Markdown files under the
    folder are treated as derived working short essays / publication material.
    Nothing in this workspace outranks theory-map or canonical mother text.
    """
    records: list[FileRecord] = []
    warnings: list[str] = []

    if not publish_root.exists():
        # The workspace is optional until short-essay work begins.
        return records, warnings

    if not publish_root.is_dir():
        warnings.append(f"Publish workspace is not a directory: {publish_root}")
        return records, warnings

    seen: set[Path] = set()

    for filename in PUBLISH_REGISTRY_FILES:
        path = publish_root / filename
        if not path.is_file():
            warnings.append(f"Publish registry not found: {path}")
            continue

        seen.add(path.resolve())
        body = read_text(path)
        role = "QUESTION_POOL" if filename == "question-pool.md" else "SHORT_ESSAY_MANIFEST"
        records.append(
            FileRecord(
                abs_path=path,
                rel_path=f"index/publish/{filename}",
                title=first_h1(body) or path.stem,
                language="unknown",
                status="WORKING",
                section="WORKING PUBLICATION REGISTRY",
                source_kind="EXTERNAL_INDEX",
                authority="WORKING_REGISTRY",
                role=role,
                note=(
                    "Local working publication registry. It routes short-essay work but "
                    "does not outrank theory-map or canonical mother text."
                ),
            )
        )

    other_md = sorted(
        (p for p in publish_root.rglob("*.md") if p.is_file() and p.resolve() not in seen),
        key=lambda p: natural_key(p.relative_to(publish_root).as_posix()),
    )

    for path in other_md:
        body = read_text(path)
        inner_rel = path.relative_to(publish_root).as_posix()
        records.append(
            FileRecord(
                abs_path=path,
                rel_path=f"index/publish/{inner_rel}",
                title=first_h1(body) or path.stem,
                language=infer_language(inner_rel),
                status="WORKING",
                section="WORKING SHORT ESSAYS",
                source_kind="EXTERNAL_INDEX",
                authority="DERIVED_WORKING",
                role="SHORT_ESSAY_WORKING",
                note=(
                    "Working short-essay/publication material. Validate against the "
                    "question pool, theory-map, and relevant canonical mother text."
                ),
            )
        )

    return records, warnings


# -----------------------------------------------------------------------------
# Ordering and writing
# -----------------------------------------------------------------------------

def count_status(records: Iterable[FileRecord], status: str) -> int:
    return sum(1 for r in records if r.status == status)


def routing_order(record: FileRecord) -> int:
    try:
        return ROUTING_DOCUMENTS.index(record.rel_path)
    except ValueError:
        return len(ROUTING_DOCUMENTS)


def split_records(
    docs_records: list[FileRecord],
    structural_records: list[FileRecord],
    publish_records: list[FileRecord],
):
    routing = sorted(
        (r for r in docs_records if r.role == "ROUTING_DOCUMENT"),
        key=routing_order,
    )

    structural_core = [r for r in structural_records if r.role == "STRUCTURAL_CORE"]
    structural_bridge = [r for r in structural_records if r.role == "STRUCTURAL_BRIDGE"]
    structural_aux = [r for r in structural_records if r.role == "STRUCTURAL_AUXILIARY"]

    publish_registries = [
        r for r in publish_records
        if r.role in {"QUESTION_POOL", "SHORT_ESSAY_MANIFEST"}
    ]
    publish_registry_order = {
        "QUESTION_POOL": 0,
        "SHORT_ESSAY_MANIFEST": 1,
    }
    publish_registries.sort(key=lambda r: publish_registry_order.get(r.role, 99))

    working_short_essays = sorted(
        (r for r in publish_records if r.role == "SHORT_ESSAY_WORKING"),
        key=lambda r: natural_key(r.rel_path),
    )

    # scan_structural_algorithm already emits zh before en and natural file order.
    public = sorted(
        (r for r in docs_records if r.status == "PUBLIC"),
        key=lambda r: r.nav_order if r.nav_order is not None else 10**9,
    )

    auxiliary_docs = [
        r
        for r in docs_records
        if r.role != "ROUTING_DOCUMENT" and r.status != "PUBLIC"
    ]
    auxiliary_docs.sort(
        key=lambda r: (
            0 if r.status == "UNPUBLISHED" else 1,
            natural_key(r.rel_path),
        )
    )

    return (
        routing,
        publish_registries,
        structural_core,
        structural_bridge,
        public,
        working_short_essays,
        auxiliary_docs,
        structural_aux,
    )


def write_file_record(out, record: FileRecord) -> None:
    body = read_text(record.abs_path)

    out.write(separator("-") + "\n")
    out.write("<<< FILE_BEGIN >>>\n\n")
    out.write(f"TITLE: {record.title}\n")
    out.write(f"PATH: {record.rel_path}\n")
    out.write(f"LANGUAGE: {record.language}\n")
    out.write(f"STATUS: {record.status}\n")
    out.write(f"SOURCE_KIND: {record.source_kind}\n")
    out.write(f"AUTHORITY: {record.authority}\n")
    out.write(f"ROLE: {record.role}\n")
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


def write_group(out, name: str, records: Sequence[FileRecord], purpose: str) -> None:
    out.write(separator() + "\n")
    out.write(f"<<< {name}_BEGIN >>>\n")
    out.write(separator() + "\n\n")
    out.write(f"COUNT: {len(records)}\n")
    out.write(f"PURPOSE: {purpose}\n\n")

    for record in records:
        write_file_record(out, record)

    out.write(separator() + "\n")
    out.write(f"<<< {name}_END >>>\n")
    out.write(separator() + "\n\n")



def write_machine_read_protocol(out) -> None:
    """Emit a short machine-facing protocol before any corpus metadata or bodies."""
    out.write("<<< MACHINE_READ_PROTOCOL_BEGIN >>>\n\n")
    out.write("FILE_TYPE: ROUTED_KNOWLEDGE_CORPUS\n")
    out.write("DEFAULT_READ_MODE: ROUTED_RETRIEVAL\n")
    out.write("FULL_SEQUENTIAL_SCAN: NOT_REQUIRED\n\n")

    out.write("BOOT_SEQUENCE:\n")
    out.write("1. Read MACHINE_READ_PROTOCOL.\n")
    out.write("2. Read CORPUS_METADATA.\n")
    out.write("3. Read AI_READING_GUIDE.\n")
    out.write("4. Read DOCUMENT_MANIFEST.\n")
    out.write("5. Read memo/theory-map.md for theory topology and article placement.\n")
    out.write("6. Read memo/file_map.md for repository paths and publication state.\n")
    out.write("7. For short-essay discovery/drafting, read index/publish/question-pool.md and index/publish/short-essay-manifest.md.\n")
    out.write("8. Stop broad sequential reading; retrieve further text only for the actual question.\n\n")

    out.write("READ_MODES:\n")
    out.write("- NORMAL: map first, then targeted retrieval. This is the default.\n")
    out.write("- FULL_AUDIT: systematic corpus-wide reading only when explicitly requested for a full audit, exhaustive consistency review, corpus-wide inventory, or cold-start stress test.\n\n")

    out.write("NORMAL_QUERY_PROTOCOL:\n")
    out.write("1. Classify the question and identify the relevant theoretical domain.\n")
    out.write("2. Route with DOCUMENT_MANIFEST plus PATH / ROLE / AUTHORITY / STATUS / title / theory terms.\n")
    out.write("3. Prefer the relevant canonical mother text over derived or public articles.\n")
    out.write("4. Read only the documents needed to answer the question.\n")
    out.write("5. Expand outward only when comparison, evidence, or contradiction checking requires it.\n\n")

    out.write("AUTHORITY_RULES:\n")
    out.write("- Theory hierarchy / article placement -> memo/theory-map.md.\n")
    out.write("- Repository paths / publication state -> memo/file_map.md.\n")
    out.write("- Concrete theoretical claim -> corresponding canonical mother text.\n")
    out.write("- Application or public text does not outrank its canonical source merely because it is newer, longer, or more specific.\n")
    out.write("- Short-essay registries are workflow/control state, not theoretical authority.\n\n")

    out.write("TOPOLOGY_GUARDRAILS:\n")
    out.write("- Physical body order is a reading order, NOT a theoretical parent-child order.\n")
    out.write("- Do NOT linearize Civilizational Structure -> Productive-Forces Economics -> Reality/Future -> Six Series.\n")
    out.write("- Productive-Forces Economics, Reality/Future Path, Six Series, and Structural Syntheses are distinct derived/projection/application branches of Civilizational Structure.\n")
    out.write("- Transition Dynamics / Movement begins after the boundary of stable structural explanation.\n")
    out.write("- Public Outputs are compiled projections and do not constitute a theory layer.\n\n")

    out.write("SHORT_ESSAY_WORKFLOW:\n")
    out.write("1. Use index/publish/question-pool.md to select or classify candidate problems.\n")
    out.write("2. Use index/publish/short-essay-manifest.md to recover existing LV identity and filename.\n")
    out.write("3. Do not assign theory authority to either registry.\n\n")

    out.write("ARTICLE_VALIDATION_PROTOCOL:\n")
    out.write("1. Identify the phenomenon and the Civilizational Structure node(s) or causal edge(s) used.\n")
    out.write("2. Check the relevant canonical mother text.\n")
    out.write("3. Separate canonical proposition, derived inference, empirical evidence, application hypothesis, and Movement/strategic speculation.\n")
    out.write("4. A claim appearing in an application article is not automatically foundational.\n")
    out.write("5. Peripheral articles are weakly coupled to one another and strongly coupled to canonical structure; do not compare every peripheral article unless the task requires it.\n\n")

    out.write("INFERENCE_RULE:\n")
    out.write("- Any model inference extending beyond canonical mother text should be labeled as inference or hypothesis.\n")
    out.write("- If an inference conflicts with canonical mother text, do not preserve it merely by labeling it an inference; revise or reject it.\n\n")

    out.write("<<< MACHINE_READ_PROTOCOL_END >>>\n\n")


def write_manifest(out, ordered_groups: Sequence[tuple[str, Sequence[FileRecord]]]) -> None:
    out.write(separator() + "\n")
    out.write("<<< DOCUMENT_MANIFEST_BEGIN >>>\n")
    out.write(separator() + "\n\n")
    out.write("The manifest follows BODY ORDER. Use it to jump, grep, or route retrieval.\n\n")

    counter = 0
    for group_name, records in ordered_groups:
        out.write(f"[{group_name}]\n")
        for record in records:
            counter += 1
            out.write(
                f"{counter:04d} | {record.authority} | {record.status} | "
                f"{record.language} | {record.rel_path} | {record.title}\n"
            )
        out.write("\n")

    out.write(f"TOTAL_BODY_DOCUMENTS: {counter}\n\n")
    out.write(separator() + "\n")
    out.write("<<< DOCUMENT_MANIFEST_END >>>\n")
    out.write(separator() + "\n\n")


def write_diagnostics(
    out,
    missing_nav: list[NavPage],
    duplicate_nav: list[tuple[NavPage, NavPage]],
    missing_commented: list[CommentedRef],
    reserved_future: list[CommentedRef],
    missing_excluded: list[str],
    unreferenced_md: list[str],
    routing_missing: list[str],
    routing_uncatalogued: list[str],
    structural_warnings: list[str],
    publish_warnings: list[str],
) -> None:
    out.write(separator() + "\n")
    out.write("<<< REPOSITORY_DIAGNOSTICS_BEGIN >>>\n")
    out.write(separator() + "\n\n")

    out.write(f"MISSING_ACTIVE_NAV_FILES: {len(missing_nav)}\n")
    for i, page in enumerate(missing_nav, 1):
        out.write(f"[MISSING ACTIVE {i:03d}] {page.rel_path} | {page.breadcrumb}\n")
    out.write("\n")

    out.write(f"DUPLICATE_ACTIVE_NAV_PATHS: {len(duplicate_nav)}\n")
    for i, (first, duplicate) in enumerate(duplicate_nav, 1):
        out.write(
            f"[DUPLICATE {i:03d}] {duplicate.rel_path} | "
            f"FIRST={first.breadcrumb} | DUPLICATE={duplicate.breadcrumb}\n"
        )
    out.write("\n")

    out.write(f"RESERVED_FUTURE_NAV_REFERENCES: {len(reserved_future)}\n")
    out.write(
        "NOTE: These commented Structural Algorithm paths intentionally reserve future "
        "public locations. Their current canonical bodies live under index/structural-algorithm.\n"
    )
    for i, ref in enumerate(reserved_future, 1):
        out.write(
            f"[RESERVED {i:03d}] {ref.rel_path} | YAML_LINE={ref.line_no}\n"
        )
    out.write("\n")

    out.write(f"MISSING_COMMENTED_REFERENCES: {len(missing_commented)}\n")
    for i, ref in enumerate(missing_commented, 1):
        out.write(
            f"[MISSING COMMENTED {i:03d}] {ref.rel_path} | "
            f"STATUS={ref.status} | YAML_LINE={ref.line_no}\n"
        )
    out.write("\n")

    out.write(f"MISSING_EXCLUDE_DOC_REFERENCES: {len(missing_excluded)}\n")
    for rel in missing_excluded:
        out.write(f"- {rel}\n")
    out.write("\n")

    out.write(f"ROUTING_DOCUMENTS_MISSING: {len(routing_missing)}\n")
    for rel in routing_missing:
        out.write(f"- {rel}\n")
    out.write("\n")

    out.write(f"ROUTING_DOCUMENTS_UNCATALOGUED: {len(routing_uncatalogued)}\n")
    for rel in routing_uncatalogued:
        out.write(f"- {rel}\n")
    out.write("\n")

    out.write(f"STRUCTURAL_SOURCE_WARNINGS: {len(structural_warnings)}\n")
    for warning in structural_warnings:
        out.write(f"- {warning}\n")
    out.write("\n")

    out.write(f"PUBLISH_WORKSPACE_WARNINGS: {len(publish_warnings)}\n")
    for warning in publish_warnings:
        out.write(f"- {warning}\n")
    out.write("\n")

    out.write(f"UNREFERENCED_MARKDOWN_FILES: {len(unreferenced_md)}\n")
    out.write("CONTENT_INCLUDED: NO\n")
    out.write(
        "RULE: docs/ Markdown not referenced by active nav, commented .md, exclude_docs, "
        "or direct routing include is diagnostic only.\n"
    )
    for rel in unreferenced_md:
        out.write(f"- {rel}\n")
    out.write("\n")

    out.write(separator() + "\n")
    out.write("<<< REPOSITORY_DIAGNOSTICS_END >>>\n")
    out.write(separator() + "\n\n")


def write_corpus(
    output_file: Path,
    repo_root: Path,
    docs_dir: Path,
    structural_root: Path,
    publish_root: Path,
    mkdocs_path: Path,
    raw_yaml: str,
    docs_records: list[FileRecord],
    structural_records: list[FileRecord],
    publish_records: list[FileRecord],
    nav_pages: list[NavPage],
    commented_refs: list[CommentedRef],
    missing_nav: list[NavPage],
    duplicate_nav: list[tuple[NavPage, NavPage]],
    missing_commented: list[CommentedRef],
    reserved_future: list[CommentedRef],
    missing_excluded: list[str],
    unreferenced_md: list[str],
    routing_missing: list[str],
    routing_uncatalogued: list[str],
    structural_warnings: list[str],
    publish_warnings: list[str],
    git_commit: str,
    git_dirty: str,
    generated_at: dt.datetime,
) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)

    (
        routing,
        publish_registries,
        structural_core,
        structural_bridge,
        public,
        working_short_essays,
        auxiliary_docs,
        structural_aux,
    ) = split_records(docs_records, structural_records, publish_records)

    all_body_records = (
        routing
        + publish_registries
        + structural_core
        + structural_bridge
        + public
        + working_short_essays
        + auxiliary_docs
        + structural_aux
    )

    ordered_groups: list[tuple[str, Sequence[FileRecord]]] = [
        ("ROUTING_DOCUMENTS", routing),
        ("WORKING_PUBLISH_REGISTRIES", publish_registries),
        ("FOUNDATIONAL_STRUCTURAL_THEORY", structural_core),
        ("STRUCTURAL_BRIDGES", structural_bridge),
        ("PUBLIC_CANONICAL_ARCHIVE", public),
        ("WORKING_SHORT_ESSAYS", working_short_essays),
        ("AUXILIARY_CATALOGUED_DOCS", auxiliary_docs),
        ("STRUCTURAL_AUXILIARY", structural_aux),
    ]

    with output_file.open("w", encoding="utf-8", newline="\n") as out:
        # 0. Hard machine-facing read protocol. This must be the first corpus content.
        write_machine_read_protocol(out)

        # 1. Metadata: compact and machine-readable.
        out.write("<<< CORPUS_METADATA >>>\n\n")
        out.write("CORPUS: Longview Archive Full Corpus\n")
        out.write("INCLUSION_MODE: HYBRID_MANIFEST\n")
        out.write("PRIMARY_READER: AI / retrieval / grep\n")
        out.write("READ_PROTOCOL_VERSION: 1.0\n")
        out.write(f"GENERATED_AT: {generated_at.isoformat(timespec='seconds')}\n")
        out.write(f"SOURCE_REPOSITORY: {repo_root}\n")
        out.write(f"SOURCE_MKDOCS: {safe_repo_relative(mkdocs_path, repo_root)}\n")
        out.write(f"SOURCE_DOCS_DIR: {safe_repo_relative(docs_dir, repo_root)}\n")
        out.write(f"SOURCE_STRUCTURAL_ROOT: {structural_root}\n")
        out.write(f"SOURCE_PUBLISH_ROOT: {publish_root}\n")
        out.write(f"SOURCE_GIT_COMMIT: {git_commit}\n")
        out.write(f"SOURCE_GIT_DIRTY: {git_dirty}\n")
        out.write(f"TOTAL_BODY_DOCUMENTS: {len(all_body_records)}\n")
        out.write(f"PUBLIC_DOCUMENTS: {count_status(all_body_records, 'PUBLIC')}\n")
        out.write(
            f"CANONICAL_UNPUBLISHED_DOCUMENTS: "
            f"{count_status(all_body_records, 'CANONICAL_UNPUBLISHED')}\n"
        )
        out.write(f"UNPUBLISHED_DOCUMENTS: {count_status(all_body_records, 'UNPUBLISHED')}\n")
        out.write(f"INTERNAL_DOCUMENTS: {count_status(all_body_records, 'INTERNAL')}\n")
        out.write(f"ROUTING_DOCUMENTS_INCLUDED: {len(routing)}/{len(ROUTING_DOCUMENTS)}\n")
        out.write(f"STRUCTURAL_CORE_DOCUMENTS: {len(structural_core)}\n")
        out.write(f"STRUCTURAL_BRIDGE_DOCUMENTS: {len(structural_bridge)}\n")
        out.write(f"WORKING_PUBLISH_REGISTRIES: {len(publish_registries)}\n")
        out.write(f"WORKING_SHORT_ESSAYS: {len(working_short_essays)}\n")
        out.write(f"RESERVED_FUTURE_NAV_REFERENCES: {len(reserved_future)}\n")
        out.write(f"ACTIVE_NAV_REFERENCES: {len(nav_pages)}\n")
        out.write(f"COMMENTED_MD_REFERENCES: {len(commented_refs)}\n")
        out.write(f"UNREFERENCED_MARKDOWN_FILES: {len(unreferenced_md)}\n")
        out.write(f"MISSING_ACTIVE_NAV_FILES: {len(missing_nav)}\n")
        out.write(f"MISSING_COMMENTED_REFERENCES: {len(missing_commented)}\n")
        out.write(f"DUPLICATE_ACTIVE_NAV_PATHS: {len(duplicate_nav)}\n\n")
        out.write("<<< CORPUS_METADATA_END >>>\n\n")

        # 2. AI reading guide before any long bodies.
        out.write(separator() + "\n")
        out.write("<<< AI_READING_GUIDE_BEGIN >>>\n")
        out.write(separator() + "\n\n")
        out.write(
            "PURPOSE: Read this corpus as an ordered authority stack, not as a flat pile of essays.\n\n"
        )
        out.write("AUTHORITY_ORDER:\n")
        out.write("1. memo/theory-map.md -> theory hierarchy and article placement\n")
        out.write("2. index/structural-algorithm/* -> foundational canonical unpublished theory\n")
        out.write("3. structural bridge essays -> derived causal bridges\n")
        out.write("4. index/publish registries -> short-essay workflow / identity routing only\n")
        out.write("5. active MkDocs pages -> current public canonical archive\n")
        out.write("6. other commented/excluded material -> auxiliary context only\n")
        out.write("7. diagnostics and raw mkdocs.yml -> repository/publication metadata\n\n")
        out.write("CONFLICT_RULES:\n")
        out.write("- Theory hierarchy conflict: memo/theory-map.md wins.\n")
        out.write("- Repository path/publication-state conflict: memo/file_map.md wins.\n")
        out.write("- Concrete argument conflict: use the corresponding canonical mother text.\n")
        out.write(
            "- Commented Structural Algorithm paths in mkdocs.yml are RESERVED FUTURE PUBLICATION "
            "SLOTS; absence under docs/ is intentional while the mother text lives in index/.\n"
        )
        out.write(
            "- 'Everything begins with productive forces' remains the material explanatory starting "
            "point; Civilizational Structure is the current foundational organizational model.\n\n"
        )
        out.write("SEARCH_HINTS:\n")
        out.write("- Grep PATH:, ROLE:, AUTHORITY:, STATUS:, or a theory term.\n")
        out.write("- Use DOCUMENT_MANIFEST for fast routing before reading long bodies.\n")
        out.write("- Do not infer publication status from physical location alone; read STATUS.\n")
        out.write("- Default to targeted retrieval; do not treat corpus body order as theoretical inheritance.\n\n")

        out.write("TOPOLOGY_REMINDER:\n")
        out.write("- Civilizational Structure is the common generative root.\n")
        out.write("- PFE, Reality/Future, Six Series, and Structural Syntheses are not a single linear parent-child chain.\n")
        out.write("- Movement begins after the stable-structure boundary; Public Outputs are compiled projections.\n\n")

        out.write("VALIDATION_REMINDER:\n")
        out.write("- For a new article, check index/publish/question-pool.md, then map it to canonical node(s)/edge(s).\n")
        out.write("- For an existing LV article, route identity through index/publish/short-essay-manifest.md.\n")
        out.write("- Separate canonical claims from derived inference, evidence, application hypothesis, and strategic speculation.\n\n")
        out.write(separator() + "\n")
        out.write("<<< AI_READING_GUIDE_END >>>\n")
        out.write(separator() + "\n\n")

        # 3. Compact manifest for AI routing / grep.
        write_manifest(out, ordered_groups)

        # 4-9. Bodies in authority order.
        write_group(
            out,
            "ROUTING_DOCUMENTS",
            routing,
            "Interpretation routers. Theory map first, repository map second.",
        )
        write_group(
            out,
            "WORKING_PUBLISH_REGISTRIES",
            publish_registries,
            "Question pool and short-essay identity manifest; workflow/control plane, not theory authority.",
        )
        write_group(
            out,
            "FOUNDATIONAL_STRUCTURAL_THEORY",
            structural_core,
            "Canonical unpublished Structural Algorithm mother texts; Chinese first, English second.",
        )
        write_group(
            out,
            "STRUCTURAL_BRIDGES",
            structural_bridge,
            "Derived bridge essays connecting foundational structure to specific causal domains.",
        )
        write_group(
            out,
            "PUBLIC_CANONICAL_ARCHIVE",
            public,
            "Current public website edition in active MkDocs nav order.",
        )
        write_group(
            out,
            "WORKING_SHORT_ESSAYS",
            working_short_essays,
            "Derived working short essays/publication files from index/publish; validate against canonical theory.",
        )
        write_group(
            out,
            "AUXILIARY_CATALOGUED_DOCS",
            auxiliary_docs,
            "Existing commented/excluded docs that are not primary routing authorities.",
        )
        write_group(
            out,
            "STRUCTURAL_AUXILIARY",
            structural_aux,
            "Submission/adaptation/readme material from the external structural source; not foundational authority.",
        )

        # 10. Diagnostics after semantic content.
        write_diagnostics(
            out,
            missing_nav=missing_nav,
            duplicate_nav=duplicate_nav,
            missing_commented=missing_commented,
            reserved_future=reserved_future,
            missing_excluded=missing_excluded,
            unreferenced_md=unreferenced_md,
            routing_missing=routing_missing,
            routing_uncatalogued=routing_uncatalogued,
            structural_warnings=structural_warnings,
            publish_warnings=publish_warnings,
        )

        # 11. Raw YAML at the end: useful for humans/grep, low priority for AI reading.
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

        out.write("<<< CORPUS_END >>>\n")


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build an AI-friendly Longview Archive corpus from website + structural mother text."
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
    parser.add_argument(
        "--structural-root",
        type=Path,
        default=None,
        help=(
            "Canonical unpublished Structural Algorithm root. "
            "Default: <repo-parent>/index/structural-algorithm"
        ),
    )
    parser.add_argument(
        "--publish-root",
        type=Path,
        default=None,
        help=(
            "Working short-essay/publication workspace. "
            "Default: <repo-parent>/index/publish"
        ),
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    script_dir = Path(__file__).resolve().parent
    repo_root = (args.repo_root or script_dir.parent).resolve()
    mkdocs_path = (args.mkdocs or (repo_root / "mkdocs.yml")).resolve()
    structural_root = (
        args.structural_root.resolve()
        if args.structural_root
        else (repo_root.parent / "index" / "structural-algorithm").resolve()
    )
    publish_root = (
        args.publish_root.resolve()
        if args.publish_root
        else (repo_root.parent / "index" / "publish").resolve()
    )

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
        docs_records,
        missing_nav,
        duplicate_nav,
        missing_commented,
        reserved_future,
        referenced_paths_list,
    ) = build_docs_records(
        docs_dir,
        nav_pages,
        commented_refs,
        excluded_md_paths,
    )

    referenced_paths = set(referenced_paths_list) | set(excluded_md_paths)
    routing_missing, routing_uncatalogued = ensure_routing_documents(
        docs_dir,
        docs_records,
        referenced_paths,
    )

    unreferenced_md = find_unreferenced_markdown(docs_dir, referenced_paths)
    structural_records, structural_warnings = scan_structural_algorithm(structural_root)
    publish_records, publish_warnings = scan_publish_workspace(publish_root)

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
        structural_root=structural_root,
        publish_root=publish_root,
        mkdocs_path=mkdocs_path,
        raw_yaml=raw_yaml,
        docs_records=docs_records,
        structural_records=structural_records,
        publish_records=publish_records,
        nav_pages=nav_pages,
        commented_refs=commented_refs,
        missing_nav=missing_nav,
        duplicate_nav=duplicate_nav,
        missing_commented=missing_commented,
        reserved_future=reserved_future,
        missing_excluded=missing_excluded,
        unreferenced_md=unreferenced_md,
        routing_missing=routing_missing,
        routing_uncatalogued=routing_uncatalogued,
        structural_warnings=structural_warnings,
        publish_warnings=publish_warnings,
        git_commit=git_commit,
        git_dirty=git_dirty,
        generated_at=generated_at,
    )

    routing_count = sum(1 for r in docs_records if r.role == "ROUTING_DOCUMENT")
    structural_core_count = sum(1 for r in structural_records if r.role == "STRUCTURAL_CORE")
    structural_bridge_count = sum(1 for r in structural_records if r.role == "STRUCTURAL_BRIDGE")
    structural_aux_count = sum(1 for r in structural_records if r.role == "STRUCTURAL_AUXILIARY")
    publish_registry_count = sum(
        1 for r in publish_records if r.role in {"QUESTION_POOL", "SHORT_ESSAY_MANIFEST"}
    )
    working_short_essay_count = sum(1 for r in publish_records if r.role == "SHORT_ESSAY_WORKING")

    print()
    print("Longview AI-friendly corpus build complete.")
    print(f"Repository                 : {repo_root}")
    print(f"Docs                       : {docs_dir}")
    print(f"Structural source          : {structural_root}")
    print(f"Publish workspace          : {publish_root}")
    print(f"Output                     : {output_file}")
    print()
    print(f"Website records            : {len(docs_records)}")
    print(f"Public website docs        : {count_status(docs_records, 'PUBLIC')}")
    print(f"Routing documents          : {routing_count}/{len(ROUTING_DOCUMENTS)}")
    print(f"Structural core            : {structural_core_count}")
    print(f"Structural bridges         : {structural_bridge_count}")
    print(f"Structural auxiliary       : {structural_aux_count}")
    print(f"Publish registries         : {publish_registry_count}/{len(PUBLISH_REGISTRY_FILES)}")
    print(f"Working short essays       : {working_short_essay_count}")
    print(f"Reserved future nav refs   : {len(reserved_future)}")
    print(f"Missing active nav files   : {len(missing_nav)}")
    print(f"Missing commented refs     : {len(missing_commented)}")
    print(f"Unreferenced docs Markdown : {len(unreferenced_md)}")
    print()

    warnings_exist = bool(
        missing_nav
        or routing_missing
        or routing_uncatalogued
        or structural_warnings
        or publish_warnings
        or structural_core_count == 0
    )

    if missing_nav:
        print("WARNING: active MkDocs nav contains missing files.")
    if routing_missing:
        print("WARNING: routing documents are missing:")
        for rel in routing_missing:
            print(f"  - {rel}")
    if routing_uncatalogued:
        print("WARNING: routing documents exist but are not catalogued in mkdocs.yml exclude_docs:")
        for rel in routing_uncatalogued:
            print(f"  - {rel}")
    for warning in structural_warnings:
        print(f"WARNING: {warning}")
    for warning in publish_warnings:
        print(f"WARNING: {warning}")
    if structural_core_count == 0:
        print("WARNING: no Structural Algorithm core Markdown was merged.")

    if warnings_exist:
        print()
        print("Corpus was generated, but its completeness/metadata should be checked.")
        return 1

    print("Corpus authority stack: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
