#!/usr/bin/env python3
from pathlib import Path


def main() -> None:
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    accessable = 0
    with path.open(encoding="utf-8") as file:
        previous_row = ""
        current_row = ""
        next_row = ""
        for raw_line in file:
            previous_row = current_row
            current_row = next_row
            next_row = raw_line.strip()
            accessable += accessable_in_row(previous_row, current_row, next_row)
    previous_row = current_row
    current_row = next_row
    next_row = ""
    accessable += accessable_in_row(previous_row, current_row, next_row)
    print(f"{accessable} rolls of paper can be accessed by a forklift.")


def accessable_in_row(previous_row, current_row, next_row):
    if not current_row:
        return 0
    result = 0
    for i, ch in enumerate(current_row):
        if ch != "@":
            continue
        neigbors = ""
        for column in range(i - 1, i + 2):
            if column < 0:
                continue
            neigbors += previous_row[column : column + 1]
            neigbors += current_row[column : column + 1]
            neigbors += next_row[column : column + 1]
        if neigbors.count("@") <= 4:
            result += 1
    return result


if __name__ == "__main__":
    main()
