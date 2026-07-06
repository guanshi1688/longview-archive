from pathlib import Path

TITLE = "# 兜底文明｜合订本\n\n"

FILES = [
    "index.md",
    "01-not-city-state-civilization.md",
    "02-myths-of-governance.md",
    "03-flood-control-and-state-capacity.md",
    "04-spring-autumn-warring-states-selection.md",
    "05-qin-system-as-organization-machine.md",
    "06-decline-of-aristocratic-clans.md",
    "07-why-central-state-suppresses-local-military-power.md",
    "08-why-chinese-dynasties-are-fallback-civilizations.md",
    "09-why-the-west-could-muddle-through.md",
    "10-great-unification-as-ultimate-order.md",
]

OUTPUT = "兜底文明｜合订本.md"


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
