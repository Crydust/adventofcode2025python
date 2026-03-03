#!/usr/bin/env python3
from pathlib import Path


def main():
    zero = 0
    minimum = 0
    maximum = 99
    current = 50
    times_pointing_at_zero = 0
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    with open(path, encoding="utf-8") as f:
        times_pointing_at_zero_sub_total = 0
        for line in f:
            line = line.strip()
            direction = line[0]
            if direction not in ("L", "R"):
                raise ValueError(f"Invalid direction: {direction!r}")
            increment = -1 if direction == "L" else 1
            amount = int(line[1:])
            for _ in range(amount):
                current = (current + increment) % (maximum + 1)
                times_pointing_at_zero_sub_total += (current == zero)
        times_pointing_at_zero += times_pointing_at_zero_sub_total
        print(f"The dial is rotated {line} to point at {current}; "
              f"during this rotation, it points at {zero} {times_pointing_at_zero_sub_total} times.")
    print(f"The dial points at {zero} a total of {times_pointing_at_zero} times.")


if __name__ == "__main__":
    main()
