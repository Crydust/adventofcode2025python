#!/usr/bin/env python3
from pathlib import Path


def main() -> None:
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    with path.open(encoding="utf-8") as f:
        total = sum(maximum_joltage_from_bank(line.strip()) for line in f)
    print(f"The total output joltage is {total}.")


def maximum_joltage_from_bank(bank: str) -> int:
    batteries = [int(i) for i in bank]
    for i in range(0, 100):
        if len(batteries) == 12:
            break
        remove_preceding_large_jolt(batteries, len(batteries) - 11)
        batteries = [n for n in batteries if n >= 0]
    return int("".join(str(n) for n in batteries[0:12]))


def remove_preceding_large_jolt(batteries: list[int], groupSize: int) -> None:
    for i in range(len(batteries) - groupSize + 1):
        highestValue = -1
        highestIndex = -1
        for j in range(i, i + groupSize):
            value = batteries[j]
            if value > highestValue:
                highestValue = value
                highestIndex = j
        if highestIndex != i and highestIndex != -1:
            for j in range(i, highestIndex):
                batteries[j] = -1
            break


if __name__ == "__main__":
    main()
