#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a local-only review bundle for 组织经济学.

Source order: index -> reading rules -> terms -> chapters 00..10.
Output is placed ONE level above this script's directory and prefixed with '_'.
Never modify the independent Markdown files or MkDocs configuration.
"""
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / '_组织经济学_中文完整合订本.md'
PREFIXES = [f'{i:02d}-' for i in range(11)]


def chapters() -> list[Path]:
    result: list[Path] = []
    for prefix in PREFIXES:
        found = [p for p in HERE.glob(prefix + '*.md') if p.is_file()]
        if len(found) != 1:
            raise RuntimeError(f'章节 {prefix} 应有且仅有一份源文件；实际找到 {len(found)} 份：{found}')
        result.append(found[0])
    return result


def main() -> int:
    front = [HERE / 'index.md', HERE / '阅读与校验规则.md', HERE / '核心术语.md']
    all_files = front + chapters()
    for file in all_files:
        if not file.is_file():
            raise FileNotFoundError(file)
    sections: list[str] = [
        '<!--\n本文件由 build_organisation_economics.py 生成，仅供本地整体审稿。\n'
        '请修改独立章节源文件，不要直接修改合订本；不要复制进网站 docs/。\n-->\n',
        '# 组织经济学｜中文完整审稿合订本\n',
        f'> 源文件：{len(all_files)} 份（总览＋阅读规则＋术语＋00—10）\n',
    ]
    for file in all_files:
        body = file.read_text(encoding='utf-8-sig').strip()
        if not re.search(r'^#\s+\S', body, re.MULTILINE):
            raise ValueError(f'没有一级标题：{file.name}')
        sections.append(f'\n<!-- SOURCE: {file.name} -->\n\n{body}\n')
    OUTPUT.write_text('\n---\n'.join(sections).rstrip() + '\n', encoding='utf-8')
    print(f'OK: {OUTPUT}\nSource Markdown: {len(all_files)}')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        raise SystemExit(2)
