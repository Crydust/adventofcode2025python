#!/usr/bin/env python3
import re
from pathlib import Path

SHAPE_INDEX_PATTERN = re.compile(r"(\d):")
SHAPE_LINE_PATTERN = re.compile(r"[.#]{3}")
REGION_PATTERN = re.compile(r"(\d+)x(\d+): (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)")


def main() -> None:
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    with path.open(encoding="utf-8") as file:
        shape_index = 0
        shape_areas = [0] * 6
        fitting_regions = 0
        for raw_line in file:
            line = raw_line.strip()

            if match := SHAPE_INDEX_PATTERN.fullmatch(line):
                shape_index = int(match.group(1))

            elif SHAPE_LINE_PATTERN.fullmatch(line):
                shape_areas[shape_index] += line.count("#")

            elif match := REGION_PATTERN.fullmatch(line):
                width, height, *region_counts = list(map(int, match.groups()))
                area = width * height
                required_area = sum(
                    count * shape_area
                    for count, shape_area in zip(region_counts, shape_areas)
                )
                if area >= required_area:
                    fitting_regions += 1

    print(f"{fitting_regions} areas can fit all the presents.")


if __name__ == "__main__":
    main()
