#!/usr/bin/env python3
import re
from pathlib import Path


def main() -> None:
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    shape_index_pattern = re.compile(r"(\d):")
    shape_line_pattern = re.compile(r"[.#]{3}")
    region_pattern = re.compile(r"(\d+)x(\d+): (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)")
    with path.open(encoding="utf-8") as file:
        shapes = [0, 0, 0, 0, 0, 0]
        shape_index = 0
        areas_that_can_fit_presents = 0
        for raw_line in file:
            line = raw_line.strip()
            if match := shape_index_pattern.fullmatch(line):
                shape_index = int(match.group(1))
            elif shape_line_pattern.fullmatch(line):
                count = 0
                for ch in line:
                    if ch == "#":
                        count += 1
                shapes[shape_index] += count
            elif match := region_pattern.fullmatch(line):
                area = int(match.group(1)) * int(match.group(2))
                totalNeeded = sum(
                    int(match.group(i + 3)) * (shapes[i]) for i in range(0, 6)
                )
                if area >= totalNeeded:
                    areas_that_can_fit_presents += 1
    print(f"{areas_that_can_fit_presents} areas can fit all the presents.")


if __name__ == "__main__":
    main()
