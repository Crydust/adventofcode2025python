#!/usr/bin/env python3
# -*- coding: utf-8 -*-
zero = 0
minimum = 0
maximum = 99
current = 50
timesPointingAtZero = 0
with open("./example.txt", encoding="utf-8") as f:
    for line in f:
        rotation = int(line[1:].strip())
        if line[0] == "L":
            rotation *= -1
        current = (current + rotation)
        if current > maximum:
            current %= (maximum + 1)
        while current < minimum:
            current += maximum + 1
        if current == zero:
            timesPointingAtZero += 1
        print(f"The dial is rotated {line.strip()} to point at {current}")
print(f"The dial points at {zero} a total of {timesPointingAtZero} times.")
