#!/usr/bin/env python3
from pathlib import Path


def main():
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    total = 0
    with path.open(encoding="utf-8") as f:
        for line in f:
            total += maximum_joltage_from_bank(line.strip())
    print(f"The total output joltage is {total}.")


def maximum_joltage_from_bank(bank: str) -> int:
    for first_battery in range(9, 0, -1):
        first_battery_index = bank.find(str(first_battery))
        if first_battery_index == -1:
            continue
        for second_battery in range(9, 0, -1):
            second_battery_index = bank.find(str(second_battery), first_battery_index + 1)
            if second_battery_index == -1:
                continue
            return first_battery * 10 + second_battery
    return 0

if __name__ == "__main__":
    main()
