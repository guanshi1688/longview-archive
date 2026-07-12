from pathlib import Path
import re

"""
Build Chinese full-reading bundles for Longview Archive.

Current public Chinese paths:

docs/essays/chinese/index.md
docs/essays/chinese/core-terms-chinese.md
docs/essays/chinese/reading-rules.md
docs/essays/chinese/reality/
docs/essays/chinese/future/

This script generates:

docs/essays/chinese/reality/reality_full.md
docs/essays/chinese/future/future_full.md

The generated full bundles are internal/review reading files.
Do not add them to public mkdocs.yml navigation unless you explicitly want to publish them.
"""


def find_repo_root() -> Path:
    """
    Find repository root by walking upward until a docs/ folder is found.

    This is more robust than Path(__file__).resolve().parents[1]:
    - works if this script is placed at repo root;
    - works if it is placed under scripts/;
    - works if it is placed under tools/.
    """
    here = Path(__file__).resolve()

    for candidate in [here.parent, *here.parents]:
        if (candidate / "docs").is_dir():
            return candidate

    raise RuntimeError("Cannot find repository root: no docs/ folder found above this script.")


ROOT = find_repo_root()
DOCS = ROOT / "docs"

CHINESE_DIR = DOCS / "essays" / "chinese"
REALITY_DIR = CHINESE_DIR / "reality"
FUTURE_DIR = CHINESE_DIR / "future"


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
    # 兼容带 For details... 与不带 For details... 的版本
    copyright_patterns = [
        # 中英版权完整块，通常由 --- 开始
        r"\n---\s*\n\s*© 2026 Longview Archive｜观势档案。.*?(?:For details, see \[Copyright｜版权声明\]\(/copyright/\)\.)?\s*$",

        # 英文版权完整块，通常由 --- 开始
        r"\n---\s*\n\s*© 2026 Longview Archive\. .*?(?:For details, see \[Copyright｜版权声明\]\(/copyright/\)\.)?\s*$",

        # 无前置 --- 的中文版权块
        r"\n\s*© 2026 Longview Archive｜观势档案。.*?(?:For details, see \[Copyright｜版权声明\]\(/copyright/\)\.)?\s*$",

        # 无前置 --- 的英文版权块
        r"\n\s*© 2026 Longview Archive\. .*?(?:For details, see \[Copyright｜版权声明\]\(/copyright/\)\.)?\s*$",
    ]

    for pattern in copyright_patterns:
        text = re.sub(pattern, "", text, flags=re.DOTALL)

    text = text.strip()

    # 2. 去掉末尾署名块
    # 先用通用新格式清理：
    # 星衡｜Aster Vale
    # Longview Archive｜观势档案
    # 任意组名
    # 2026.07
    generic_signature_patterns = [
        r"\n\s*星衡｜Aster Vale\s*\n\s*Longview Archive｜观势档案\s*\n\s*[^\n]+?\s*\n\s*2026\.07\s*$",

        r"\n\s*星衡｜Aster Vale<br>\s*\n?Longview Archive｜观势档案<br>\s*\n?[^\n<]+(?:｜[^\n<]+)?<br>\s*\n?2026\.07\s*$",
    ]

    for pattern in generic_signature_patterns:
        text = re.sub(pattern, "", text, flags=re.MULTILINE)

    # 旧署名格式：带分隔线
    legacy_signature_patterns = [
        r"\n---\s*\n\s*星衡 / Aster Vale\s*\nX\.H\s*\n星衡札记・Aster Vale Notes\s*\n\s*于上海\s*\n2026/[67]\s*$",

        r"\n星衡 / Aster Vale\s*\nX\.H\s*\n星衡札记・Aster Vale Notes\s*\n\s*于上海\s*\n2026/[67]\s*$",
    ]

    for pattern in legacy_signature_patterns:
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
    """
    Read article file inside a group directory.

    Reality 08 had once appeared in mkdocs.yml as 08s.md.
    To avoid breaking older local trees, this function allows a fallback from
    08.md to 08s.md. Prefer normalizing the actual repo file to 08.md.
    """
    path = source_dir / filename

    fallback_names = {
        "08.md": ["08s.md"],
    }

    if not path.exists():
        for alt in fallback_names.get(filename, []):
            alt_path = source_dir / alt
            if alt_path.exists():
                print(f"Using fallback file for {filename}: {alt_path}")
                path = alt_path
                break

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

    # 合订本前置内容：中文入口 + 中文核心术语 + 阅读规则
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
        "essays/chinese/index.md",
        "essays/chinese/core-terms-chinese.md",
        "essays/chinese/reading-rules.md",
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

本合订本作为独立阅读版本，已前置收录《中文入口｜Longview Essays｜长线观势》《中文核心术语》与《阅读规则》，用于统一核心变量、概念边界与阅读坐标。

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

本合订本作为独立阅读版本，已前置收录《中文入口｜Longview Essays｜长线观势》《中文核心术语》与《阅读规则》，用于统一核心变量、概念边界与阅读坐标。

Future Path｜未来之路 与 Reality｜现实世界 不是两套理论，而是同一套底层概念在另一方向上的展开。""",
        footer_group="Future Path｜未来之路",
        prefix_files=common_prefix,
    )


if __name__ == "__main__":
    main()
