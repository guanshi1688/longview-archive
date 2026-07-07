# -*- coding: utf-8 -*-
"""
Build merged Markdown file for the current essay series.

Usage:
    python build.py

Output:
    _build/扩张的边界-合订本.md
"""

from pathlib import Path
import re
from datetime import datetime


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "_build"
OUT_FILE = OUT_DIR / "扩张的边界-合订本.md"

SERIES_TITLE = "扩张的边界"
COPYRIGHT = "版权说明：本文为 Longview Archive｜观势档案 中文札记材料。未经许可，不得转载、改写、翻译、商用或重新发布。"


def article_sort_key(path: Path):
    """
    Sort files by numeric prefix.
    Example:
        01-border.md -> 1
        10-final.md -> 10
    """
    match = re.match(r"^(\d+)-", path.name)
    if match:
        return int(match.group(1))
    return 9999


def clean_article_text(text: str) -> str:
    """
    Remove repeated copyright block from individual articles
    so the combined file only has one final copyright statement.
    """
    text = text.replace("\ufeff", "")
    text = text.strip()

    patterns = [
        r"\n---\s*\n版权说明：本文为 Longview Archive｜观势档案 中文札记材料。未经许可，不得转载、改写、翻译、商用或重新发布。\s*$",
        r"\n版权说明：本文为 Longview Archive｜观势档案 中文札记材料。未经许可，不得转载、改写、翻译、商用或重新发布。\s*$",
    ]

    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.S)

    return text.strip()


def collect_articles():
    """
    Only collect numbered Markdown files.
    This avoids accidentally merging index.md or generated files.
    """
    files = [
        p for p in ROOT.glob("*.md")
        if re.match(r"^\d{2}-.*\.md$", p.name)
    ]

    files.sort(key=article_sort_key)
    return files


def extract_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def build():
    articles = collect_articles()

    if not articles:
        raise RuntimeError("没有找到 01- 到 10- 开头的 Markdown 文章。")

    OUT_DIR.mkdir(exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    parts = []
    toc = []

    parts.append(f"# {SERIES_TITLE}｜合订本\n")
    parts.append("本文档由 `build.py` 自动生成，用于内部归档、校对和合订本预览。\n")
    parts.append(f"生成时间：{now}\n")
    parts.append("---\n")
    parts.append("## 目录\n")

    cleaned_articles = []

    for idx, path in enumerate(articles, start=1):
        raw = path.read_text(encoding="utf-8")
        cleaned = clean_article_text(raw)
        title = extract_title(cleaned, path.stem)

        anchor = f"article-{idx:02d}"
        toc.append(f"{idx}. [{title}](#{anchor})")
        cleaned_articles.append((anchor, title, path, cleaned))

    parts.extend(toc)
    parts.append("\n---\n")

    for anchor, title, path, cleaned in cleaned_articles:
        parts.append(f'<a id="{anchor}"></a>\n')
        parts.append(f"<!-- Source: {path.name} -->\n\n")
        parts.append(cleaned)
        parts.append("\n\n---\n")

    parts.append(f"\n{COPYRIGHT}\n")

    OUT_FILE.write_text("\n".join(parts), encoding="utf-8")

    print(f"合并完成：{OUT_FILE}")
    print(f"文章数量：{len(articles)}")


if __name__ == "__main__":
    build()
