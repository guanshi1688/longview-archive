from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

REALITY_DIR = DOCS / "essays" / "reality"
FUTURE_DIR = DOCS / "essays" / "future"


def clean_article(text: str) -> str:
    """
    合订本清理规则：
    1. 去掉每篇末尾版权声明，避免合订本重复版权。
    2. 去掉每篇末尾署名块，避免合订本重复署名。
    3. 去掉清理后可能残留的末尾分隔线。
    4. 保留每篇标题和正文。
    """

    text = text.strip()

    # 1. 去掉末尾版权声明块
    # 标准版权块通常从 --- 开始，到 For details... 结束
    copyright_patterns = [
        # 中英版权完整块：中文在前，英文在后
        r"\n---\s*\n\s*© 2026 Longview Archive｜观势档案。.*?For details, see \[Copyright｜版权声明\]\(/copyright/\)\.\s*$",

        # 英文版权在前的版本
        r"\n---\s*\n\s*© 2026 Longview Archive\. .*?For details, see \[Copyright｜版权声明\]\(/copyright/\)\.\s*$",

        # 如果没有前置 ---，也清理
        r"\n\s*© 2026 Longview Archive｜观势档案。.*?For details, see \[Copyright｜版权声明\]\(/copyright/\)\.\s*$",

        r"\n\s*© 2026 Longview Archive\. .*?For details, see \[Copyright｜版权声明\]\(/copyright/\)\.\s*$",
    ]

    for pattern in copyright_patterns:
        text = re.sub(pattern, "", text, flags=re.DOTALL)

    text = text.strip()

    # 2. 去掉末尾署名块
    signature_patterns = [
        # Reality：普通 Markdown 换行
        r"\n\s*星衡｜Aster Vale\s*\nLongview Archive｜观势档案\s*\nReality｜现实世界\s*\n2026\.07\s*$",

        # Future Path：普通 Markdown 换行
        r"\n\s*星衡｜Aster Vale\s*\nLongview Archive｜观势档案\s*\nFuture Path｜未来之路\s*\n2026\.07\s*$",

        # Longview Essays / 总览等
        r"\n\s*星衡｜Aster Vale\s*\nLongview Archive｜观势档案\s*\nLongview Essays｜长线观势\s*\n2026\.07\s*$",

        # Core Terms / 理论术语等
        r"\n\s*星衡｜Aster Vale\s*\nLongview Archive｜观势档案\s*\nCore Terms｜理论核心术语\s*\n2026\.07\s*$",

        # Reading Rules / 阅读评判规则等
        r"\n\s*星衡｜Aster Vale\s*\nLongview Archive｜观势档案\s*\nHow to Read This Framework｜阅读评判规则\s*\n2026\.07\s*$",

        # Reality：HTML <br> 换行
        r"\n\s*星衡｜Aster Vale<br>\s*\n?Longview Archive｜观势档案<br>\s*\n?Reality｜现实世界<br>\s*\n?2026\.07\s*$",

        # Future Path：HTML <br> 换行
        r"\n\s*星衡｜Aster Vale<br>\s*\n?Longview Archive｜观势档案<br>\s*\n?Future Path｜未来之路<br>\s*\n?2026\.07\s*$",

        # Longview Essays：HTML <br> 换行
        r"\n\s*星衡｜Aster Vale<br>\s*\n?Longview Archive｜观势档案<br>\s*\n?Longview Essays｜长线观势<br>\s*\n?2026\.07\s*$",

        # Core Terms：HTML <br> 换行
        r"\n\s*星衡｜Aster Vale<br>\s*\n?Longview Archive｜观势档案<br>\s*\n?Core Terms｜理论核心术语<br>\s*\n?2026\.07\s*$",

        # Reading Rules：HTML <br> 换行
        r"\n\s*星衡｜Aster Vale<br>\s*\n?Longview Archive｜观势档案<br>\s*\n?How to Read This Framework｜阅读评判规则<br>\s*\n?2026\.07\s*$",

        # 旧署名格式：带分隔线
        r"\n---\s*\n\s*星衡 / Aster Vale\s*\nX\.H\s*\n星衡札记・Aster Vale Notes\s*\n\s*于上海\s*\n2026/7\s*$",

        # 旧署名格式：无分隔线
        r"\n星衡 / Aster Vale\s*\nX\.H\s*\n星衡札记・Aster Vale Notes\s*\n\s*于上海\s*\n2026/7\s*$",
    ]

    for pattern in signature_patterns:
        text = re.sub(pattern, "", text, flags=re.MULTILINE)

    text = text.strip()

    # 3. 去掉末尾可能残留的分隔线
    text = re.sub(r"\n---\s*$", "", text).strip()

    return text


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
    parts: list[str] = []

    parts.append(f"# {title}\n")
    parts.append(intro.strip())
    parts.append("\n\n---\n")

    # 合订本前置内容：总览 + Core Terms + 阅读评判规则
    if prefix_files:
        for relative_path in prefix_files:
            text = read_doc(relative_path)
            if text:
                parts.append(text)
                parts.append("\n\n---\n")

    # 本组合订正文
    for filename in files:
        text = read_group_file(source_dir, filename)
        if text:
            parts.append(text)
            parts.append("\n\n---\n")

    # 合订本统一署名 + 统一版权声明
    parts.append(
        f"""星衡｜Aster Vale<br>
Longview Archive｜观势档案<br>
{footer_group}<br>
2026.07

---

© 2026 Longview Archive｜观势档案。除特别说明外，本文采用 CC BY-NC-ND 4.0 许可协议：允许署名非商业分享，禁止未经授权的改写、翻译、重组与商业使用。

© 2026 Longview Archive. Unless otherwise stated, this essay is licensed under CC BY-NC-ND 4.0: attribution required, non-commercial sharing only, no unauthorized modifications, translations, reorganizations, or commercial use.

For details, see [Copyright｜版权声明](/copyright/).
"""
    )

    output_path = source_dir / output_file
    output_path.write_text("\n".join(parts).strip() + "\n", encoding="utf-8")

    print(f"Generated: {output_path}")


def main():
    common_prefix = [
        "essays/index.md",
        "core-terms.md",
        "essays/reading-rules.md",
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

本合订本作为独立阅读版本，已前置收录《总览｜Longview Essays｜长线观势》《Core Terms｜理论核心术语》与《How to Read This Framework｜阅读评判规则》，用于统一核心变量、概念边界与阅读坐标。

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

本合订本作为独立阅读版本，已前置收录《总览｜Longview Essays｜长线观势》《Core Terms｜理论核心术语》与《How to Read This Framework｜阅读评判规则》，用于统一核心变量、概念边界与阅读坐标。

Future Path｜未来之路 与 Reality｜现实世界 不是两套理论，而是同一套底层概念在另一方向上的展开。""",
        footer_group="Future Path｜未来之路",
        prefix_files=common_prefix,
    )


if __name__ == "__main__":
    main()
