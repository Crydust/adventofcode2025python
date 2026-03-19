#!/usr/bin/env python3
from typing import Iterator


def sliding_windows(rows: list[str]) -> Iterator[tuple[str, str, str]]:
    """Yield (previous_row, current_row, next_row) tuples."""
    previous = ""
    current = ""
    for next_ in rows:
        if current:
            yield previous, current, next_
        previous, current = current, next_
    if current:
        yield previous, current, ""


def is_accessible(previous: str, current: str, next_: str, col: int) -> bool:
    return (
        0 <= col < len(current)
        and current[col] == "@"
        and _count_neighbors(previous, current, next_, col) <= 4
    )


def _count_neighbors(previous: str, current: str, next_: str, col: int) -> int:
    """Count '@' neighbors around a position."""
    return sum(
        1
        for row in (previous, current, next_)
        for column in range(col - 1, col + 2)
        if 0 <= column < len(row)
        if row[column] == "@"
    )
