from pathlib import Path
import re

"""
Build a full review bundle for the English Framework folder.

Place this file here:

docs/essays/english/build.py

Run from this folder or from repo root:

python build.py

It generates:

docs/essays/english/_english-framework-bundle.md

This bundle is for internal review. Do not add it to mkdocs.yml unless you
explicitly want to publish the combined version.
"""

BASE = Path(__file__).resolve().parent

OUTPUT_FILE = "_english-framework-bundle.md"

# Logical reading order for the English Framework layer.
ORDER = [
    ("Reader Map", "reader-map.md"),
    ("Common Ground", "common-ground.md"),
    ("Core Terms", "core-terms-eng.md"),
    ("Framework Overview", "index.md"),
    ("Productive Forces and Civilization", "geography-productive-forces-and-civilization.md"),
    ("Civilizational Metabolism", "civilizational-metabolism.md"),
    ("Absorptive Capacity", "absorptive-capacity.md"),
    ("Surplus, Absorption, and Reproduction", "surplus-absorption-and-reproduction.md"),
    ("Value Capture and the Western System", "western-system.md"),
]


def clean_article(text: str) -> str:
    """
    Remove repeated end signatures and copyright blocks from each article,
    so the combined bundle has only one final signature/copyright notice.
    """

    text = text.strip()

    # Remove final copyright block, with or without "For details..."
    copyright_patterns = [
        r"\n---\s*\n\s*© 2026 Longview Archive｜观势档案。.*?(?:For details, see \[Copyright｜版权声明\]\(/copyright/\)\.)?\s*$",
        r"\n---\s*\n\s*© 2026 Longview Archive\. .*?(?:For details, see \[Copyright｜版权声明\]\(/copyright/\)\.)?\s*$",
        r"\n\s*© 2026 Longview Archive｜观势档案。.*?(?:For details, see \[Copyright｜版权声明\]\(/copyright/\)\.)?\s*$",
        r"\n\s*© 2026 Longview Archive\. .*?(?:For details, see \[Copyright｜版权声明\]\(/copyright/\)\.)?\s*$",
    ]

    for pattern in copyright_patterns:
        text = re.sub(pattern, "", text, flags=re.DOTALL)

    text = text.strip()

    # Remove common Longview signature blocks:
    # Aster Vale
    # Longview Archive｜观势档案
    # <group>
    # 2026.07
    signature_patterns = [
        r"\n\s*Aster Vale\s*\n\s*Longview Archive｜观势档案\s*\n\s*[^\n]+?\s*\n\s*2026\.07\s*$",
        r"\n\s*星衡｜Aster Vale\s*\n\s*Longview Archive｜观势档案\s*\n\s*[^\n]+?\s*\n\s*2026\.07\s*$",
        r"\n\s*Aster Vale<br>\s*\n?Longview Archive｜观势档案<br>\s*\n?[^\n<]+(?:｜[^\n<]+)?<br>\s*\n?2026\.07\s*$",
        r"\n\s*星衡｜Aster Vale<br>\s*\n?Longview Archive｜观势档案<br>\s*\n?[^\n<]+(?:｜[^\n<]+)?<br>\s*\n?2026\.07\s*$",
    ]

    for pattern in signature_patterns:
        text = re.sub(pattern, "", text, flags=re.MULTILINE)

    # Remove repeated final separator if left behind.
    text = re.sub(r"\n---\s*$", "", text).strip()

    return text


def read_file(filename: str) -> str:
    path = BASE / filename

    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")

    return clean_article(path.read_text(encoding="utf-8"))


def collect_unknown_markdown_files() -> list[str]:
    """
    Include extra markdown files at the end if they exist in the folder but are
    not listed in ORDER. This prevents accidental omission during review.
    """
    ordered = {filename for _, filename in ORDER}
    ignored = {
        OUTPUT_FILE,
        Path(__file__).name,
    }

    extras = []

    for path in sorted(BASE.glob("*.md")):
        if path.name in ordered or path.name in ignored:
            continue

        # Skip internal/generated bundles by default.
        if path.name.startswith("_"):
            continue

        extras.append(path.name)

    return extras


def build() -> None:
    parts: list[str] = []

    parts.append("# English Framework｜Full Review Bundle\n")
    parts.append(
        """This file is an internal review bundle for the English Framework layer of Longview Archive.

It combines the orientation pages, core terms, foundational framework essays, and the Western System essay in a fixed reading order.

Do not treat this as a separate public essay unless it is intentionally published later."""
    )
    parts.append("\n\n---\n")

    missing = []

    for label, filename in ORDER:
        path = BASE / filename
        if not path.exists():
            missing.append(filename)
            continue

        text = read_file(filename)
        if text:
            parts.append(f"<!-- Source: {filename} | {label} -->\n")
            parts.append(text)
            parts.append("\n\n---\n")

    extras = collect_unknown_markdown_files()
    if extras:
        parts.append("# Additional Files Not Listed in ORDER\n")
        parts.append("The following files were found in this folder but are not part of the fixed Framework order.\n")
        parts.append("\n\n---\n")

        for filename in extras:
            text = read_file(filename)
            if text:
                parts.append(f"<!-- Source: {filename} | Extra -->\n")
                parts.append(text)
                parts.append("\n\n---\n")

    if missing:
        parts.append("# Missing Files\n")
        for filename in missing:
            parts.append(f"- `{filename}`")
        parts.append("\n\n---\n")

    parts.append(
        """Aster Vale<br>
Longview Archive｜观势档案<br>
English Framework｜Full Review Bundle<br>
2026.07

---

© 2026 Longview Archive｜观势档案。除特别说明外，本文采用 CC BY-NC-ND 4.0 许可协议：允许署名非商业分享，禁止未经授权的改写、翻译、重组与商业使用。

© 2026 Longview Archive. Unless otherwise stated, this essay is licensed under CC BY-NC-ND 4.0: attribution required, non-commercial sharing only, no unauthorized modifications, translations, reorganizations, or commercial use.

For details, see [Copyright｜版权声明](/copyright/).
"""
    )

    output_path = BASE / OUTPUT_FILE
    output_path.write_text("\n".join(parts).strip() + "\n", encoding="utf-8")

    print(f"Generated: {output_path}")

    if missing:
        print("\nWarning: missing files:")
        for filename in missing:
            print(f"  - {filename}")

    if extras:
        print("\nExtra markdown files appended at the end:")
        for filename in extras:
            print(f"  - {filename}")


if __name__ == "__main__":
    build()
