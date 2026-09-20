#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Longview AI Bootstrap and Corpus from *individual* canonical Markdown.

Source policy (2026-09-20):
  1. Structural Algorithm / skeleton: 52 individual Markdown sources in the
     sibling index/structural-algorithm/ directory (26 in each language).
  2. Organisation Economics / operating manual: the 14 Chinese and 14 English
     individual pages in the ACTIVE mkdocs.yml nav, sourced from docs/.
  3. Public projections and other public pages: remaining ACTIVE nav pages only.

NO other source is included: no commented nav bodies, hidden bridges, old
Productive-Forces Economics, unreferenced docs/, index/publish/, routing memo
bodies, generated bundles, or raw mkdocs.yml. Non-source files remain untouched.
The Bootstrap is self-contained and does not import stale theory-map text.

Default layout:
  <git-root>/longview-archive/scripts/build_corpus.py
  <git-root>/longview-archive/mkdocs.yml
  <git-root>/longview-archive/docs/
  <git-root>/index/structural-algorithm/chinese|english/
  <git-root>/index/current/corpus/Longview_{Bootstrap,Corpus}_<timestamp>.md

Requires: pip install PyYAML
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any, TextIO

try:
    import yaml
except ImportError:
    print("ERROR: Install PyYAML: python -m pip install PyYAML", file=sys.stderr)
    raise SystemExit(2)

MANUAL_PREFIXES = (
    "essays/chinese/organisation_economics/",
    "essays/english/organisation_economics/",
)
RETIRED_PREFIXES = (
    "essays/chinese/productive-forces-economics/",
    "essays/english/productive-forces-economics/",
)
STANDALONE_PREFIXES = (
    "essays/chinese/standalone/",
    "essays/english/standalone/",
)
EXPECTED_STRUCTURAL_PER_LANGUAGE = 26
EXPECTED_MANUAL_PER_LANGUAGE = 14
STRUCTURAL_LAYOUT: dict[str, dict[str, Any]] = {
    "chinese": {
        "lang": "zh",
        "front": ("阅读与校验规则.md", "核心术语.md"),
        "common_00": "00-生产力的组织形式与文明投影*.md",
        "common_12": "文明结构算法_12_总结*.md",
        "series": (
            ("CHINA", ("china", "Chinese_CN_Civilizational_Structure"), "文明结构算法_生产型组织_{n:02d}_*.md"),
            ("WESTERN", ("western", "Western_CN_Civilizational_Structure"), "文明结构算法_接口型组织_{n:02d}_*.md"),
        ),
    },
    "english": {
        "lang": "en",
        "front": ("Reading_and_Verification_Rules.md", "Core_Terms.md"),
        "common_00": "00_*.md",
        "common_12": "12_*.md",
        "series": (
            ("CHINA", ("china", "Chinese_Civilizational_Structure"), "{n:02d}_*.md"),
            ("WESTERN", ("western", "Western_Civilizational_Structure"), "{n:02d}_*.md"),
        ),
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def relative(value: str) -> str:
    raw = value.strip().replace("\\", "/").lstrip("./")
    path = PurePosixPath(raw)
    if path.is_absolute() or ".." in path.parts or not raw:
        raise ValueError(f"Unsafe nav path: {value!r}")
    return path.as_posix()


def natural_key(s: str) -> list[Any]:
    return [int(x) if x.isdigit() else x.lower() for x in re.split(r"(\d+)", s)]


def first_heading(body: str, fallback: str) -> str:
    for line in body.splitlines():
        match = re.match(r"^\s*#\s+(.+?)\s*$", line)
        if match:
            return match.group(1)
    return fallback


def language(rel: str) -> str:
    parts = PurePosixPath(rel).parts
    if "chinese" in parts:
        return "zh"
    if "english" in parts:
        return "en"
    return "unknown"


def is_bundle(rel: str) -> bool:
    """Reject generated review bundles even if inadvertently placed in the nav."""
    p = PurePosixPath(rel)
    name = p.stem.lower()
    parts = [x.lower() for x in p.parts]
    return (
        "合订本" in rel
        or "bundle" in name
        or "bundles" in parts
        or "合订" in name
        or name.startswith("_frontiers-")
        or name.startswith("_value-capture-")
    )


def retired(rel: str) -> bool:
    low = rel.lower()
    return any(low.startswith(prefix) for prefix in RETIRED_PREFIXES)


def flatten_nav(nav: Any) -> list[tuple[str, str, str]]:
    """Return (title, Markdown path, breadcrumbs) from active YAML only."""
    result: list[tuple[str, str, str]] = []

    def visit(value: Any, crumbs: list[str]) -> None:
        if isinstance(value, list):
            for item in value:
                visit(item, crumbs)
        elif isinstance(value, dict):
            for title, child in value.items():
                if isinstance(child, str):
                    if not child.lower().endswith(".md"):
                        continue
                    result.append((str(title), relative(child), " / ".join(crumbs + [str(title)])))
                else:
                    visit(child, crumbs + [str(title)])
        elif isinstance(value, str) and value.lower().endswith(".md"):
            rel = relative(value)
            result.append((PurePosixPath(rel).stem, rel, " / ".join(crumbs)))

    visit(nav, [])
    return result


def make_record(path: Path, rel: str, title: str, lang: str,
                role: str, authority: str, status: str, section: str,
                nav_order: int | None = None) -> dict[str, Any]:
    return {
        "path": path,
        "rel": rel,
        "title": title,
        "lang": lang,
        "role": role,
        "authority": authority,
        "status": status,
        "section": section,
        "nav_order": nav_order,
    }


def scan_active_nav(docs_dir: Path, nav: Any) -> tuple[list[dict[str, Any]], list[str], list[str]]:
    """The active nav is the sole website-article whitelist."""
    entries = flatten_nav(nav)
    records: list[dict[str, Any]] = []
    warnings: list[str] = []
    skipped: list[str] = []
    seen: set[str] = set()

    for pos, (nav_title, rel, crumb) in enumerate(entries, 1):
        if rel in seen:
            warnings.append(f"Duplicate active nav path (body included once): {rel}")
            continue
        seen.add(rel)
        if retired(rel):
            skipped.append(f"RETIRED: {rel}")
            continue
        if is_bundle(rel):
            skipped.append(f"GENERATED_BUNDLE: {rel}")
            continue
        path = docs_dir / Path(*PurePosixPath(rel).parts)
        if not path.is_file():
            warnings.append(f"Missing ACTIVE mkdocs.yml page: {rel} | {crumb}")
            continue
        manual = any(rel.startswith(prefix) for prefix in MANUAL_PREFIXES)
        standalone = any(rel.startswith(prefix) for prefix in STANDALONE_PREFIXES)
        role = "ORGANISATION_MANUAL" if manual else (
            "PUBLIC_STANDALONE" if standalone else "PUBLIC_ARCHIVE"
        )
        authority = "OPERATIONAL_MANUAL" if manual else "PUBLIC_PROJECTION"
        section = "ORGANISATION ECONOMICS / MANUAL" if manual else crumb
        records.append(make_record(
            path, rel, nav_title, language(rel), role, authority,
            "PUBLIC", section, pos,
        ))

    for lang, prefix in (("zh", MANUAL_PREFIXES[0]), ("en", MANUAL_PREFIXES[1])):
        count = sum(r["rel"].startswith(prefix) for r in records)
        if count != EXPECTED_MANUAL_PER_LANGUAGE:
            warnings.append(
                f"Incomplete {lang} Organisation Economics manual: "
                f"{count}/{EXPECTED_MANUAL_PER_LANGUAGE} active individual Markdown pages."
            )
    return records, warnings, skipped


def scan_structural(root: Path) -> tuple[list[dict[str, Any]], list[str]]:
    """The ONLY body inclusion outside the active MkDocs nav."""
    records: list[dict[str, Any]] = []
    warnings: list[str] = []

    for dirname, layout in STRUCTURAL_LAYOUT.items():
        lang_dir = root / dirname
        if not lang_dir.is_dir():
            warnings.append(f"Missing structural language directory: {lang_dir}")
            continue
        picked: list[tuple[Path, str]] = []

        def pick(folder: Path, glob: str, section: str) -> None:
            matches = sorted((p for p in folder.glob(glob) if p.is_file() and
                              not is_bundle(p.name)), key=lambda p: natural_key(p.name))
            if len(matches) != 1:
                warnings.append(
                    f"Structural source must match EXACTLY ONCE: {folder / glob} "
                    f"| found {len(matches)}: {[p.name for p in matches]}"
                )
            else:
                picked.append((matches[0], section))

        for item in layout["front"]:
            pick(lang_dir, item, f"SHARED / {item}")
        pick(lang_dir, layout["common_00"], "SHARED 00 / GENERATIVE MODEL")
        for series, aliases, pattern in layout["series"]:
            folders = [lang_dir / alias for alias in aliases if (lang_dir / alias).is_dir()]
            if len(folders) != 1:
                warnings.append(
                    f"Expected one structural {dirname}/{series} folder "
                    f"from {aliases}; found {[str(p) for p in folders]}"
                )
                continue
            for n in range(1, 12):
                pick(folders[0], pattern.format(n=n), f"{series} / {n:02d}")
        pick(lang_dir, layout["common_12"], "SHARED 12 / SYNTHESIS")

        if len(picked) != EXPECTED_STRUCTURAL_PER_LANGUAGE:
            warnings.append(
                f"Incomplete {dirname} structural skeleton: "
                f"{len(picked)}/{EXPECTED_STRUCTURAL_PER_LANGUAGE} sources."
            )
        for path, section in picked:
            rel = f"index/structural-algorithm/{dirname}/{path.relative_to(lang_dir).as_posix()}"
            records.append(make_record(
                path, rel, first_heading(read_text(path), path.stem),
                layout["lang"], "STRUCTURAL_CORE", "FOUNDATIONAL_CANONICAL",
                "CANONICAL_UNPUBLISHED", f"CIVILIZATIONAL STRUCTURAL ALGORITHM / {section}",
            ))
    return records, warnings


def group_records(structural: list[dict[str, Any]], public: list[dict[str, Any]]) -> list[tuple[str, list[dict[str, Any]]]]:
    manual = [r for r in public if r["role"] == "ORGANISATION_MANUAL"]
    other = [r for r in public if r["role"] != "ORGANISATION_MANUAL"]
    return [
        ("CIVILIZATIONAL_STRUCTURAL_ALGORITHM_SKELETON", structural),
        ("ORGANISATION_ECONOMICS_OPERATING_MANUAL", manual),
        ("YAML_ACTIVE_PUBLIC_ARTICLES", other),
    ]


def protocol(out: TextIO, bootstrap_name: str, corpus_name: str) -> None:
    out.write("<<< MACHINE_READ_PROTOCOL_BEGIN >>>\n\n")
    out.write("FILE_TYPE: LONGVIEW_ROUTED_KNOWLEDGE_CORPUS\n")
    out.write("READ_MODE: MANIFEST_FIRST / TARGETED_RETRIEVAL\n")
    out.write(f"BOOTSTRAP: {bootstrap_name}\nFULL_CORPUS: {corpus_name}\n\n")
    out.write("CURRENT_THEORY_TOPOLOGY:\n")
    out.write("1. Civilizational Structural Algorithm = GENERATIVE SKELETON / foundational explanation.\n")
    out.write("2. Organisation Economics = OPERATING MANUAL / economic language and mechanisms, NOT a deeper founding ontology.\n")
    out.write("3. All other active-nav articles = PUBLIC PROJECTIONS / specific applications and evidence; not another theory layer.\n")
    out.write("The shared material basis is sustained production and reproduction.\n")
    out.write("The skeleton models long-run organisational selection; the manual examines the operation and reproduction of capacity, people, interfaces and social absorption.\n")
    out.write("Order of bodies is retrieval order, not proof of a strict causal chain through each article.\n\n")
    out.write("SOURCE_RULES:\n")
    out.write("- Only structural-algorithm individual local sources + active mkdocs.yml nav Markdown are included.\n")
    out.write("- Old Productive-Forces Economics is RETIRED, preserved in Git but excluded from this corpus.\n")
    out.write("- Commented YAML entries, unreferenced Markdown, index/publish, private memos, hidden bridges, bundles and review compilations are excluded.\n")
    out.write("- Source pages only; raw YAML is not appended and stale theory-map content is not imported.\n")
    out.write("- Shared structural 00 and 12 occur ONCE in each language; 01-11 China and Western are distinct lines.\n")
    out.write("- Independently retrieve a specific source and verify historical claims; a projection cannot overwrite foundational definitions.\n")
    out.write("<<< MACHINE_READ_PROTOCOL_END >>>\n\n")


def manifest(out: TextIO, groups: list[tuple[str, list[dict[str, Any]]]]) -> None:
    out.write("<<< DOCUMENT_MANIFEST_BEGIN >>>\n\n")
    index = 0
    for name, records in groups:
        out.write(f"[{name}] COUNT: {len(records)}\n")
        for r in records:
            index += 1
            out.write(
                f"{index:04d} | {r['authority']} | {r['status']} | {r['lang']} "
                f"| {r['rel']} | {r['title']}\n"
            )
        out.write("\n")
    out.write(f"TOTAL_BODY_DOCUMENTS: {index}\n")
    out.write("<<< DOCUMENT_MANIFEST_END >>>\n\n")


def write_record(out: TextIO, rec: dict[str, Any]) -> None:
    body = read_text(rec["path"])
    out.write("-" * 90 + "\n<<< FILE_BEGIN >>>\n\n")
    for field, key in (("TITLE", "title"), ("PATH", "rel"),
                       ("LANGUAGE", "lang"), ("STATUS", "status"),
                       ("AUTHORITY", "authority"), ("ROLE", "role"),
                       ("SECTION", "section")):
        out.write(f"{field}: {rec[key]}\n")
    if rec["nav_order"] is not None:
        out.write(f"NAV_ORDER: {rec['nav_order']}\n")
    out.write("\n<<< CONTENT_BEGIN >>>\n\n")
    out.write(body)
    if not body.endswith("\n"):
        out.write("\n")
    out.write("\n<<< CONTENT_END >>>\n<<< FILE_END >>>\n\n")


def git_meta(repo: Path) -> tuple[str, str]:
    def run(*args: str) -> str | None:
        try:
            return subprocess.run(
                ["git", "-C", str(repo), *args], check=True,
                capture_output=True, text=True, encoding="utf-8", errors="replace",
            ).stdout.strip()
        except (FileNotFoundError, subprocess.CalledProcessError):
            return None
    return run("rev-parse", "--short", "HEAD") or "UNKNOWN", (
        "UNKNOWN" if (s := run("status", "--porcelain")) is None
        else "YES" if s else "NO"
    )


def diagnostics(out: TextIO, problems: list[str], skipped: list[str]) -> None:
    out.write("<<< BUILD_DIAGNOSTICS_BEGIN >>>\n")
    out.write(f"WARNINGS: {len(problems)}\n")
    for p in problems:
        out.write(f"- {p}\n")
    out.write(f"GUARD_SKIPPED_ACTIVE_NAV: {len(skipped)}\n")
    for s in skipped:
        out.write(f"- {s}\n")
    out.write("<<< BUILD_DIAGNOSTICS_END >>>\n")


def main() -> int:
    p = argparse.ArgumentParser(description="Build Longview: local structural skeleton + YAML-active individual Markdown only.")
    p.add_argument("--repo-root", type=Path, default=None)
    p.add_argument("--mkdocs", type=Path, default=None)
    p.add_argument("--structural-root", type=Path, default=None)
    p.add_argument("--output-dir", type=Path, default=None)
    # Keep old CLI calls accepted. This directory is NEVER ingested as a body source.
    p.add_argument("--publish-root", type=Path, default=None,
                   help="Legacy compatibility only; index/publish is no longer ingested.")
    args = p.parse_args()
    repo = (args.repo_root or Path(__file__).resolve().parent.parent).resolve()
    mkdocs = (args.mkdocs or repo / "mkdocs.yml").resolve()
    structural = (args.structural_root or repo.parent / "index" / "structural-algorithm").resolve()
    out_dir = (args.output_dir or repo.parent / "index" / "current" / "corpus").resolve()

    if not mkdocs.is_file():
        print(f"ERROR: Missing YAML: {mkdocs}", file=sys.stderr)
        return 2
    try:
        config = yaml.safe_load(read_text(mkdocs))
    except yaml.YAMLError as exc:
        print(f"ERROR: Invalid YAML: {exc}", file=sys.stderr)
        return 2
    if not isinstance(config, dict) or not isinstance(config.get("nav"), list):
        print("ERROR: mkdocs.yml must contain an active nav list.", file=sys.stderr)
        return 2
    docs = (repo / str(config.get("docs_dir", "docs"))).resolve()
    if not docs.is_dir():
        print(f"ERROR: docs directory missing: {docs}", file=sys.stderr)
        return 2
    website, website_warnings, skipped = scan_active_nav(docs, config["nav"])
    skeleton, skeleton_warnings = scan_structural(structural)
    problems = website_warnings + skeleton_warnings
    groups = group_records(skeleton, website)
    count = sum(len(g) for _, g in groups)

    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.now().astimezone()
    stamp = timestamp.strftime("%Y-%m-%d_%H%M%S")
    bootstrap = out_dir / f"Longview_Bootstrap_{stamp}.md"
    corpus = out_dir / f"Longview_Corpus_{stamp}.md"
    if bootstrap.exists() or corpus.exists():
        print(f"ERROR: Output timestamp already exists: {stamp}", file=sys.stderr)
        return 2
    commit, dirty = git_meta(repo)

    with bootstrap.open("w", encoding="utf-8", newline="\n") as f:
        protocol(f, bootstrap.name, corpus.name)
        f.write("<<< BOOTSTRAP_METADATA >>>\n")
        f.write(f"GENERATED_AT: {timestamp.isoformat(timespec='seconds')}\n")
        f.write(f"SOURCE_REPOSITORY: {repo}\nSOURCE_MKDOCS: {mkdocs}\n")
        f.write(f"SOURCE_STRUCTURAL_ROOT: {structural}\n")
        f.write(f"SOURCE_GIT_COMMIT: {commit}\nSOURCE_GIT_DIRTY: {dirty}\n")
        f.write(f"TOTAL_BODY_DOCUMENTS: {count}\n")
        for name, g in groups:
            f.write(f"{name}: {len(g)}\n")
        f.write("<<< BOOTSTRAP_METADATA_END >>>\n\n")
        manifest(f, groups)
        diagnostics(f, problems, skipped)
        f.write("\nNEXT_ACTION: Use the paired Full Corpus for targeted Markdown retrieval by PATH / ROLE.\n")

    with corpus.open("w", encoding="utf-8", newline="\n") as f:
        protocol(f, bootstrap.name, corpus.name)
        f.write("<<< CORPUS_METADATA >>>\n")
        f.write(f"GENERATED_AT: {timestamp.isoformat(timespec='seconds')}\n")
        f.write("INCLUSION_MODE: ACTIVE_YAML_PLUS_LOCAL_STRUCTURAL_INDIVIDUAL_FILES\n")
        f.write(f"SOURCE_MKDOCS: {mkdocs}\n")
        f.write(f"SOURCE_STRUCTURAL_ROOT: {structural}\n")
        f.write(f"TOTAL_BODY_DOCUMENTS: {count}\n")
        for name, g in groups:
            f.write(f"{name}: {len(g)}\n")
        f.write("<<< CORPUS_METADATA_END >>>\n\n")
        manifest(f, groups)
        for name, g in groups:
            f.write("=" * 90 + f"\n<<< {name}_BEGIN >>>\nCOUNT: {len(g)}\n\n")
            for rec in g:
                write_record(f, rec)
            f.write(f"<<< {name}_END >>>\n\n")
        diagnostics(f, problems, skipped)

    print("Longview Bootstrap + Full Corpus generated.")
    print(f"Bootstrap : {bootstrap}")
    print(f"Corpus    : {corpus}")
    print(f"Total     : {count}")
    for name, g in groups:
        print(f"  {name}: {len(g)}")
    print(f"Warnings  : {len(problems)}; guarded skip: {len(skipped)}")
    for item in problems:
        print(f"WARNING: {item}")
    for item in skipped:
        print(f"GUARD SKIP: {item}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
