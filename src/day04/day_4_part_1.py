#!/usr/bin/env python3
from pathlib import Path
from day04.utils import is_accessible, sliding_windows


def main() -> None:
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    rows = path.read_text(encoding="utf-8").splitlines()

    accessible = sum(
        accessible_in_row(prev, curr, next_)
        for prev, curr, next_ in sliding_windows(rows)
    )

    print(f"{accessible} rolls of paper can be accessed by a forklift.")


def accessible_in_row(previous: str, current: str, next_: str) -> int:
    return sum(
        1
        for col in range(len(current))
        if is_accessible(previous, current, next_, col)
    )


if __name__ == "__main__":
    main()
