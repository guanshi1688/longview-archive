from __future__ import annotations

from pathlib import Path
import sys


BASE_DIR = Path(__file__).resolve().parent

FILES = [
    "index.md",
    "00-c-methodological-memorandum.md",
    "from-Geography-to-Consumption.md",
    "01-c-western-economics.md",
    "02-c-chinese-governance.md",
    "03-c-failure.md",
    "04-c-system-contribution.md",
    "05-c-consumption.md",
    "06-c-market-generation.md",
    "07-c-inefficiency.md",
    "08-c-correction.md",
    "09-c-modernization.md",
]

OUTPUT_FILE = "_生产力经济学-合订本.md"

# 内部审稿合订本默认删除每篇重复的署名与版权尾注。
# 如需完全原样拼接，改为 False。
STRIP_REPEATED_FOOTERS = True

FOOTER_MARKERS = (
    "\n---\n\n星衡｜Aster Vale",
    "\n---\n\nAster Vale",
    "\n---\n\nEvan Vale",
)


def read_markdown(path: Path) -> str:
    """安全读取 UTF-8 / UTF-8 BOM Markdown 文件。"""
    return path.read_text(encoding="utf-8-sig").strip()


def strip_footer(text: str) -> str:
    """删除独立文章末尾重复的署名与版权区。"""
    if not STRIP_REPEATED_FOOTERS:
        return text.rstrip()

    positions: list[int] = []

    for marker in FOOTER_MARKERS:
        position = text.find(marker)
        if position != -1:
            positions.append(position)

    if not positions:
        return text.rstrip()

    return text[: min(positions)].rstrip()


def validate_sources() -> list[Path]:
    """确认所有源文件存在。"""
    paths = [BASE_DIR / filename for filename in FILES]
    missing = [path.name for path in paths if not path.is_file()]

    if missing:
        print("生成失败，缺少以下文件：", file=sys.stderr)
        for filename in missing:
            print(f"  - {filename}", file=sys.stderr)
        raise SystemExit(1)

    return paths


def build_bundle() -> Path:
    """按既定顺序生成内部合订本。"""
    source_paths = validate_sources()
    sections: list[str] = []

    for path in source_paths:
        content = strip_footer(read_markdown(path))
        sections.append(content)

    bundle_header = """<!--
本文件由 build.py 自动生成，仅供内部整体审稿。
请勿直接修改本文件。
如需修改，请编辑独立源文件后重新运行 build.py。
-->

# 生产力经济学｜完整审稿合订本

"""

    bundle = bundle_header + "\n\n---\n\n".join(sections)
    bundle = bundle.rstrip() + "\n"

    output_path = BASE_DIR / OUTPUT_FILE
    output_path.write_text(bundle, encoding="utf-8")

    return output_path


def main() -> None:
    output_path = build_bundle()
    size_kb = output_path.stat().st_size / 1024

    print(f"已生成：{output_path.name}")
    print(f"源文件：{len(FILES)} 个")
    print(f"大小：{size_kb:.1f} KB")


if __name__ == "__main__":
    main()
