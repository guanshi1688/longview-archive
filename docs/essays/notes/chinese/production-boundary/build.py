from pathlib import Path

TITLE = "# 生产的边界｜合订本\n\n"

FILES = [
    "index.md",
    "01-roads-do-not-equal-industrialization.md",
    "02-factories-do-not-equal-manufacturing-system.md",
    "03-electricity-does-not-equal-industrial-capacity.md",
    "04-population-does-not-equal-market.md",
    "05-resource-rich-countries-and-industrialization.md",
    "06-industrial-parks-as-islands.md",
    "07-cheap-labor-does-not-equal-manufacturing-advantage.md",
    "08-industrial-transfer-is-harder-than-building-factories.md",
    "09-why-china-manufacturing-cannot-be-copied-by-supply-chains.md",
    "10-production-capacity-as-civilizational-capacity.md",
]

OUTPUT = "生产的边界｜合订本.md"


def main():
    base = Path(__file__).parent
    parts = [TITLE]

    for filename in FILES:
        path = base / filename
        if not path.exists():
            print(f"缺少文件：{filename}")
            continue

        text = path.read_text(encoding="utf-8").strip()
        parts.append(text)
        parts.append("\n\n---\n\n")

    output_path = base / OUTPUT
    output_path.write_text("".join(parts).strip() + "\n", encoding="utf-8")

    print(f"已生成：{OUTPUT}")


if __name__ == "__main__":
    main()
