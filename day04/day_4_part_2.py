#!/usr/bin/env python3
from dataclasses import dataclass
from pathlib import Path


def main() -> None:
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    current_text = path.read_text(encoding="utf-8")

    rows = []
    next_rows = current_text.splitlines()
    total_removed = 0
    removed = -1

    while removed != 0:
        rows, next_rows = next_rows, []
        removed = 0
        previous_row, current_row, next_row = "", "", ""
        for row in rows:
            previous_row, current_row, next_row = current_row, next_row, row
            if not current_row:
                continue
            altered_row = remove_in_row(previous_row, current_row, next_row)
            next_rows.append(altered_row.row)
            removed += altered_row.removed
        previous_row, current_row, next_row = current_row, next_row, ""
        altered_row = remove_in_row(previous_row, current_row, next_row)
        next_rows.append(altered_row.row)
        removed += altered_row.removed
        total_removed += removed

    print(f"{total_removed} rolls of paper removed by a forklift.")


def remove_in_row(previous_row: str, current_row: str, next_row: str) -> "AlteredRow":
    copy = current_row
    removed = 0
    for i, ch in enumerate(current_row):
        if ch != "@":
            continue
        neighbor_count = 0
        for row in (previous_row, current_row, next_row):
            for column in range(i - 1, i + 2):
                if 0 <= column < len(row) and row[column] == "@":
                    neighbor_count += 1
        if neighbor_count <= 4:
            removed += 1
            copy = copy[:i] + "x" + copy[i + 1 :]
    return AlteredRow(copy, removed)


@dataclass(frozen=True)
class AlteredRow:
    row: str
    removed: int


if __name__ == "__main__":
    main()
