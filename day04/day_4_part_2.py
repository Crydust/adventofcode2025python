#!/usr/bin/env python3
import itertools
from pathlib import Path


def main() -> None:
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    rows = path.read_text(encoding="utf-8").splitlines()

    total_removed = 0
    # prime the loop
    removed = 1

    while removed:
        rows, removed = process_pass(rows)
        total_removed += removed

    print(f"{total_removed} rolls of paper removed by a forklift.")


def process_pass(rows: list[str]) -> tuple[list[str], int]:
    updated_rows: list[str] = []
    removed_total = 0

    previous_row = ""
    current_row = ""

    # sentinel flushes final pending current_row
    for next_row in itertools.chain(rows, ("",)):
        if current_row:
            updated_row, removed_in_row = remove_in_row(
                previous_row, current_row, next_row
            )
            updated_rows.append(updated_row)
            removed_total += removed_in_row

        previous_row, current_row = current_row, next_row

    return updated_rows, removed_total


def remove_in_row(
    previous_row: str, current_row: str, next_row: str
) -> tuple[str, int]:
    updated_row = list(current_row)
    removed_in_row = 0

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
            updated_row[i] = "x"
            removed_in_row += 1

    return "".join(updated_row), removed_in_row


if __name__ == "__main__":
    main()
