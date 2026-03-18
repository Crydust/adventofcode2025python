#!/usr/bin/env python3
import itertools
from pathlib import Path
from typing import Iterator


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


def sliding_windows(rows: list[str]) -> Iterator[tuple[str, str, str]]:
    """Yield (previous_row, current_row, next_row) tuples."""
    previous = ""
    current = ""
    for next_ in itertools.chain(rows, ("",)):
        if current:
            yield previous, current, next_
        previous, current = current, next_


def remove_in_row(previous: str, current: str, next_: str) -> tuple[str, int]:
    updated_row = list(current)
    removed_in_row = 0

    for col, ch in enumerate(current):
        if ch == "@" and count_neighbors(previous, current, next_, col) <= 4:
            updated_row[col] = "x"
            removed_in_row += 1

    return "".join(updated_row), removed_in_row


def count_neighbors(previous: str, current: str, next_: str, col: int) -> int:
    return sum(
        1
        for row in (previous, current, next_)
        for column in range(col - 1, col + 2)
        if 0 <= column < len(row)
        if row[column] == "@"
    )


if __name__ == "__main__":
    main()
