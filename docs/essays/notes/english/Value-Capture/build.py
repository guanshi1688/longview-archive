from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent

SERIES_DIR = ROOT / "docs" / "essays" / "notes" / "english" / "Value-Capture"

SERIES_TITLE = "The Architecture of Value Capture"

FILES = [
    ("index.md", "The Architecture of Value Capture"),
    ("01-why-producing-more-does-not-mean-earning-more.md", "Why Producing More Does Not Mean Earning More"),
    ("02-why-value-is-captured-at-the-interface.md", "Why Value Is Captured at the Interface"),
    ("03-why-pricing-power-matters-more-than-output.md", "Why Pricing Power Matters More Than Output"),
    ("04-why-finance-can-command-production-without-owning-it.md", "Why Finance Can Command Production Without Owning It"),
    ("05-why-standards-become-invisible-infrastructure.md", "Why Standards Become Invisible Infrastructure"),
    ("06-why-platforms-capture-markets-without-bearing-production.md", "Why Platforms Capture Markets Without Bearing Production"),
    ("07-why-brands-turn-production-into-hierarchy.md", "Why Brands Turn Production into Hierarchy"),
    ("08-why-legal-systems-and-compliance-shape-global-value.md", "Why Legal Systems and Compliance Shape Global Value"),
    ("09-why-reserve-currencies-are-civilizational-interfaces.md", "Why Reserve Currencies Are Civilizational Interfaces"),
    ("10-why-mature-markets-defend-value-capture.md", "Why Mature Markets Defend Value Capture"),
    ("11-why-the-global-rentier-system-faces-a-production-shock.md", "Why the Global Rentier System Faces a Production Shock"),
]


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text


def extract_h1(path: Path) -> str | None:
    if not path.exists():
        return None

    text = path.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)

    if match:
        return match.group(1).strip()

    return None


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def build_manifest():
    items = []

    for filename, title in FILES:
        path = SERIES_DIR / filename
        h1 = extract_h1(path)

        word_count = 0
        if path.exists():
            word_count = count_words(path.read_text(encoding="utf-8", errors="ignore"))

        items.append(
            {
                "file": filename,
                "title": title,
                "exists": path.exists(),
                "h1": h1,
                "h1_matches": h1 == title if h1 else False,
                "word_count": word_count,
                "relative_path": str(path.relative_to(ROOT)).replace("\\", "/"),
            }
        )

    manifest = {
        "series": SERIES_TITLE,
        "directory": str(SERIES_DIR.relative_to(ROOT)).replace("\\", "/"),
        "count": len(FILES),
        "complete": all(item["exists"] for item in items),
        "total_word_count": sum(item["word_count"] for item in items),
        "items": items,
    }

    out_path = SERIES_DIR / "manifest.json"
    out_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return manifest, out_path


def build_combined_markdown(manifest):
    out_path = SERIES_DIR / "combined.md"

    lines = []

    lines.append(f"# {SERIES_TITLE}")
    lines.append("")
    lines.append("> Combined draft for structural review.")
    lines.append("")
    lines.append("## Review Notes")
    lines.append("")
    lines.append("This file is generated automatically from the series source files.")
    lines.append("")
    lines.append("Use this combined version to review:")
    lines.append("")
    lines.append("- overall structure")
    lines.append("- repeated arguments")
    lines.append("- weak transitions")
    lines.append("- title consistency")
    lines.append("- conceptual progression")
    lines.append("- series-level rhythm")
    lines.append("")
    lines.append("## Table of Contents")
    lines.append("")

    for item in manifest["items"]:
        if item["exists"]:
            anchor = slugify(item["title"])
            lines.append(f"- [{item['title']}](#{anchor})")
        else:
            lines.append(f"- MISSING: {item['title']}")

    lines.append("")
    lines.append("---")
    lines.append("")

    for index, item in enumerate(manifest["items"]):
        path = SERIES_DIR / item["file"]

        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append(f"<!-- Source: {item['file']} -->")
        lines.append(f"<!-- Word count: {item['word_count']} -->")
        lines.append("")

        if not path.exists():
            lines.append(f"# MISSING: {item['title']}")
            lines.append("")
            continue

        text = path.read_text(encoding="utf-8", errors="ignore").strip()

        # 保持原文，不改标题、不改正文
        lines.append(text)
        lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")

    return out_path


def print_report(manifest, manifest_path: Path, combined_path: Path):
    print()
    print(f"Series: {manifest['series']}")
    print(f"Directory: {manifest['directory']}")
    print(f"Manifest: {manifest_path.relative_to(ROOT)}")
    print(f"Combined: {combined_path.relative_to(ROOT)}")
    print(f"Total word count: {manifest['total_word_count']}")
    print()

    missing = [item for item in manifest["items"] if not item["exists"]]
    h1_mismatch = [
        item
        for item in manifest["items"]
        if item["exists"] and not item["h1_matches"]
    ]

    if not missing:
        print("OK: all files exist.")
    else:
        print("Missing files:")
        for item in missing:
            print(f"  - {item['file']}")

    if h1_mismatch:
        print()
        print("H1 mismatch:")
        for item in h1_mismatch:
            print(f"  - {item['file']}")
            print(f"    expected: {item['title']}")
            print(f"    found:    {item['h1']}")

    print()
    print("Word count:")
    for item in manifest["items"]:
        print(f"  - {item['file']}: {item['word_count']} words")

    print()
    print("MkDocs nav snippet:")
    print()
    print("      - The Architecture of Value Capture:")
    for item in manifest["items"]:
        nav_path = item["relative_path"].replace("docs/", "", 1)
        print(f"          - {item['title']}: {nav_path}")


def main():
    if not SERIES_DIR.exists():
        raise FileNotFoundError(f"Series directory not found: {SERIES_DIR}")

    manifest, manifest_path = build_manifest()
    combined_path = build_combined_markdown(manifest)
    print_report(manifest, manifest_path, combined_path)


if __name__ == "__main__":
    main()
