#!/usr/bin/env python3
import re
from pathlib import Path
from typing import Any
from dataclasses import dataclass


def main():
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    product_id_ranges = read_product_id_ranges(path)
    print(product_id_ranges)
    invalid_id_pattern = re.compile(r"(.{1,9})\1")
    invalid_id_sum = 0
    for product_id_range in product_id_ranges:
        sub_list_of_invalid_ids = []
        for i in range(product_id_range.first_id_int(), product_id_range.last_id_int() + 1):
            s = str(i)
            if invalid_id_pattern.fullmatch(s):
                sub_list_of_invalid_ids.append(s)
                invalid_id_sum += i
        print(f"{product_id_range} has {len(sub_list_of_invalid_ids)} invalid IDs, {sub_list_of_invalid_ids}.");
    print(f"Adding up all the invalid IDs in this example produces {invalid_id_sum}.")


def read_product_id_ranges(path: Path) -> list[Any]:
    product_id_ranges = []
    with open(path, encoding="utf-8") as f:
        for pair in f.readline().strip().split(","):
            first_id, last_id = pair.split("-")
            product_id_ranges.append(ProductIdRange(first_id, last_id))
    return product_id_ranges


class ProductIdRange:
    def __init__(self, first_id: str, last_id: str):
        self.first_id = first_id
        self.last_id = last_id

    def first_id_int(self) -> int:
        return int(self.first_id)

    def last_id_int(self) -> int:
        return int(self.last_id)

    def __repr__(self) -> str:
        return f"{self.first_id}-{self.last_id}"


if __name__ == "__main__":
    main()
