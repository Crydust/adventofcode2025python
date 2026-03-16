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

    while trim_prefix_before_max(batteries):
        continue

    return int("".join(map(str, batteries[:12])))


def trim_prefix_before_max(batteries: list[int]) -> bool:
    """Remove the prefix before the first non-leading maximum candidate.

    Scans each window large enough to leave 12 batteries overall. When the
    largest value in a window is not already at the window start, deletes the
    batteries before that value and returns True. Returns False if no removal
    is possible.
    """
    if len(batteries) <= 12:
        return False

    group_size = len(batteries) - 11
    for start in range(len(batteries) - group_size + 1):
        end = start + group_size
        highest_index = max(range(start, end), key=batteries.__getitem__)

        if highest_index != start:
            del batteries[start:highest_index]
            return True

    return False


if __name__ == "__main__":
    main()
