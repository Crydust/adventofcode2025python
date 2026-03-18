#!/usr/bin/env python3
import itertools
from pathlib import Path
from typing import Iterator


def main() -> None:
    path = Path(__file__).with_name("example.txt")
    # path = Path(__file__).with_name("input.txt")
    rows = path.read_text(encoding="utf-8").splitlines()

    accessible = sum(
        accessible_in_row(prev, curr, next_)
        for prev, curr, next_ in sliding_windows(rows)
    )

    print(f"{accessible} rolls of paper can be accessed by a forklift.")


def sliding_windows(rows:list[str]) -> Iterator[tuple[str, str, str]]:
    """Yield (previous_row, current_row, next_row) tuples."""
    previous = ""
    current = ""
    for next_ in itertools.chain(rows, ("",)):
        if current:
            yield previous, current, next_
        previous, current = current, next_


def accessible_in_row(previous: str, current: str, next_: str) -> int:
    return sum(
        1
        for col, ch in enumerate(current)
        if ch == "@"
        if count_neighbors(previous, current, next_, col) <= 4
    )


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
