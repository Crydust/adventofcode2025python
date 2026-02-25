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
        for line in f:
            line = line.strip()
            direction = line[0]
            amount = int(line[1:])
            if direction == "L":
                amount = -amount
            range_size = maximum + 1
            current = (current + amount) % range_size
            if current == zero:
                times_pointing_at_zero += 1
            print(f"The dial is rotated {line} to point at {current}")
    print(f"The dial points at {zero} a total of {times_pointing_at_zero} times.")


if __name__ == "__main__":
    main()
