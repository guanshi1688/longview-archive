from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

REALITY_DIR = DOCS / "essays" / "reality"
FUTURE_DIR = DOCS / "essays" / "future"


def clean_article(text: str) -> str:
    """
    合订本清理规则：
    1. 去掉每篇末尾署名块，避免合订本里重复署名。
    2. 保留每篇标题和正文。
    """

    patterns = [
        # 新署名格式：Reality
        r"\n---\s*\n\s*星衡｜Aster Vale\s*\nLongview Archive｜观势档案\s*\nReality｜现实世界\s*\n2026\.07\s*$",

        # 新署名格式：Future Path
        r"\n---\s*\n\s*星衡｜Aster Vale\s*\nLongview Archive｜观势档案\s*\nFuture Path｜未来之路\s*\n2026\.07\s*$",

        # 无分隔线版本：Reality
        r"\n星衡｜Aster Vale\s*\nLongview Archive｜观势档案\s*\nReality｜现实世界\s*\n2026\.07\s*$",

        # 无分隔线版本：Future Path
        r"\n星衡｜Aster Vale\s*\nLongview Archive｜观势档案\s*\nFuture Path｜未来之路\s*\n2026\.07\s*$",

        # 旧署名格式
        r"\n---\s*\n\s*星衡 / Aster Vale\s*\nX\.H\s*\n星衡札记・Aster Vale Notes\s*\n\s*于上海\s*\n2026/7\s*$",

        # 旧署名格式，无分隔线
        r"\n星衡 / Aster Vale\s*\nX\.H\s*\n星衡札记・Aster Vale Notes\s*\n\s*于上海\s*\n2026/7\s*$",
    ]

    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.MULTILINE)

    return text.strip()


def read_doc(relative_path: str) -> str:
    path = DOCS / relative_path

    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")

    return clean_article(path.read_text(encoding="utf-8"))


def read_group_file(source_dir: Path, filename: str) -> str:
    path = source_dir / filename

    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")

    return clean_article(path.read_text(encoding="utf-8"))


def build_full(
    source_dir: Path,
    files: list[str],
    output_file: str,
    title: str,
    intro: str,
    footer_group: str,
    prefix_files: list[str] | None = None,
):
    parts = []

    parts.append(f"# {title}\n")
    parts.append(intro.strip())
    parts.append("\n\n---\n")

    # 合订本前置内容：总览 + Core Terms
    if prefix_files:
        for relative_path in prefix_files:
            text = read_doc(relative_path)
            parts.append(text)
            parts.append("\n\n---\n")

    # 本组合订正文
    for filename in files:
        text = read_group_file(source_dir, filename)
        parts.append(text)
        parts.append("\n\n---\n")

    parts.append(
        f"""星衡｜Aster Vale  
Longview Archive｜观势档案  
{footer_group}  
2026.07
"""
    )

    output_path = source_dir / output_file
    output_path.write_text("\n".join(parts).strip() + "\n", encoding="utf-8")

    print(f"Generated: {output_path}")


def main():
    common_prefix = [
        "essays/index.md",
        "core-terms/index.md",
    ]

    build_full(
        source_dir=REALITY_DIR,
        files=[
            "00.md",
            "01.md",
            "02.md",
            "03.md",
            "04.md",
            "05.md",
            "06.md",
            "07.md",
            "08.md",
            "09.md",
            "10.md",
            "11.md",
        ],
        output_file="reality_full.md",
        title="Reality｜现实世界｜合订本",
        intro="""本文为 Reality｜现实世界 组文章的连续阅读与归档版本。  
分篇阅读请使用左侧目录。

本合订本作为独立阅读版本，已前置收录《总览｜Longview Essays｜长线观势》与《Core Terms｜理论核心术语》，用于统一核心变量、概念边界与阅读坐标。

Reality｜现实世界 用于说明旧世界为什么走到边界。""",
        footer_group="Reality｜现实世界",
        prefix_files=common_prefix,
    )

    build_full(
        source_dir=FUTURE_DIR,
        files=[
            "00.md",
            "01.md",
            "02.md",
            "03.md",
            "04.md",
            "05.md",
            "06.md",
            "07.md",
            "08.md",
            "09.md",
            "10.md",
        ],
        output_file="future_full.md",
        title="Future Path｜未来之路｜合订本",
        intro="""本文为 Future Path｜未来之路 组文章的连续阅读与归档版本。  
分篇阅读请使用左侧目录。

本合订本作为独立阅读版本，已前置收录《总览｜Longview Essays｜长线观势》与《Core Terms｜理论核心术语》，用于统一核心变量、概念边界与阅读坐标。

Future Path｜未来之路 与 Reality｜现实世界 不是两套理论，而是同一套底层概念在另一方向上的展开。""",
        footer_group="Future Path｜未来之路",
        prefix_files=common_prefix,
    )


if __name__ == "__main__":
    main()
