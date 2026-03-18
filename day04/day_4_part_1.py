#!/usr/bin/env python3
from pathlib import Path


def main() -> None:
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    accessible = 0
    with path.open(encoding="utf-8") as file:
        previous_row = ""
        current_row = ""
        next_row = ""
        for raw_line in file:
            previous_row, current_row = current_row, next_row
            next_row = raw_line.strip()
            accessible += accessible_in_row(previous_row, current_row, next_row)
    previous_row, current_row, next_row = current_row, next_row, ""
    accessible += accessible_in_row(previous_row, current_row, next_row)
    print(f"{accessible} rolls of paper can be accessed by a forklift.")


def accessible_in_row(previous_row: str, current_row: str, next_row: str) -> int:
    result = 0
    for i, ch in enumerate(current_row):
        if ch != "@":
            continue
        neighbor_count = 0
        for row in (previous_row, current_row, next_row):
            for column in range(i - 1, i + 2):
                if 0 <= column < len(row) and row[column] == "@":
                    neighbor_count += 1
        if neighbor_count <= 4:
            result += 1
    return result


if __name__ == "__main__":
    main()
