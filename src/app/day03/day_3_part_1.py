#!/usr/bin/env python3
from pathlib import Path

NINE_TO_ONE = "".join(str(i) for i in range(9, 0, -1))


def main() -> None:
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    with path.open(encoding="utf-8") as file:
        total = sum(maximum_joltage_from_bank(line.strip()) for line in file)
    print(f"The total output joltage is {total}.")


def maximum_joltage_from_bank(bank: str) -> int:
    for first in NINE_TO_ONE:
        try:
            first_index = bank.index(first)
        except ValueError:
            continue

        for second in NINE_TO_ONE:
            if second in bank[first_index + 1 :]:
                return int(first + second)

    return 0


if __name__ == "__main__":
    main()
