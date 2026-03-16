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
    for i in range(0, 100):
        if len(batteries) == 12:
            break
        remove_preceding_large_jolt(batteries, len(batteries) - 11)
        batteries = [n for n in batteries if n >= 0]
    return int("".join(str(n) for n in batteries[0:12]))


def remove_preceding_large_jolt(batteries: list[int], group_size: int) -> None:
    for i in range(len(batteries) - group_size + 1):
        highest_value = -1
        highest_index = -1
        for j in range(i, i + group_size):
            value = batteries[j]
            if value > highest_value:
                highest_value = value
                highest_index = j
        if highest_index != i and highest_index != -1:
            for j in range(i, highest_index):
                batteries[j] = -1
            break


if __name__ == "__main__":
    main()
