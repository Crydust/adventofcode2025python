#!/usr/bin/env python3
from pathlib import Path
from .utils import is_accessible, sliding_windows


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

    for previous, current, next_ in sliding_windows(rows):
        updated_row, removed_in_row = remove_in_row(previous, current, next_)
        updated_rows.append(updated_row)
        removed_total += removed_in_row

    return updated_rows, removed_total


def remove_in_row(previous: str, current: str, next_: str) -> tuple[str, int]:
    updated_row = list(current)
    removed_in_row = 0

    for col in range(len(current)):
        if is_accessible(previous, current, next_, col):
            updated_row[col] = "x"
            removed_in_row += 1

    return "".join(updated_row), removed_in_row


if __name__ == "__main__":
    main()
