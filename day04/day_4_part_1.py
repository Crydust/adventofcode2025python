#!/usr/bin/env python3
import itertools
from pathlib import Path


def main() -> None:
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    rows = path.read_text(encoding="utf-8").splitlines()

    accessible = 0

    previous_row = ""
    current_row = ""

    # sentinel flushes final pending current_row
    for next_row in itertools.chain(rows, ("",)):
        accessible += accessible_in_row(previous_row, current_row, next_row)
        previous_row, current_row = current_row, next_row

    print(f"{accessible} rolls of paper can be accessed by a forklift.")


def accessible_in_row(previous_row: str, current_row: str, next_row: str) -> int:
    result = 0

    for i, ch in enumerate(current_row):
        if ch != "@":
            continue

        neighbor_count = sum(
            1
            for row in (previous_row, current_row, next_row)
            for column in range(i - 1, i + 2)
            if 0 <= column < len(row)
            if row[column] == "@"
        )

        if neighbor_count <= 4:
            result += 1

    return result


if __name__ == "__main__":
    main()
