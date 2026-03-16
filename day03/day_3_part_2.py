#!/usr/bin/env python3
from pathlib import Path


def main() -> None:
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    with path.open(encoding="utf-8") as file:
        total = sum(maximum_joltage_from_bank(line.strip()) for line in file)
    print(f"The total output joltage is {total}.")


def maximum_joltage_from_bank(bank: str) -> int:
    batteries = [int(ch) for ch in bank]

    while remove_preceding_large_jolt(batteries):
        continue

    return int("".join(map(str, batteries[:12])))


def remove_preceding_large_jolt(batteries: list[int]) -> bool:
    if len(batteries) <= 12:
        return False

    group_size = len(batteries) - 11
    for start in range(12):
        end = start + group_size
        highest_index = max(range(start, end), key=batteries.__getitem__)

        if highest_index != start:
            del batteries[start:highest_index]
            return True

    return False


if __name__ == "__main__":
    main()
