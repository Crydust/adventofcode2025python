#!/usr/bin/env python3
import re
from dataclasses import dataclass
from pathlib import Path


def main():
    # path = Path(__file__).with_name("example.txt")
    path = Path(__file__).with_name("input.txt")
    product_id_ranges = read_product_id_ranges(path)
    invalid_id_pattern = re.compile(r"(.{1,9})\1")
    total_invalid_sum = 0
    for item in product_id_ranges:
        sub_list_of_invalid_ids = [
            i for i in range(item.first_id, item.last_id + 1)
            if invalid_id_pattern.fullmatch(str(i))
        ]
        total_invalid_sum += sum(sub_list_of_invalid_ids)
        print(f"{item} has {len(sub_list_of_invalid_ids)} invalid IDs, {sub_list_of_invalid_ids}.")
    print(f"Adding up all the invalid IDs in this example produces {total_invalid_sum}.")


def read_product_id_ranges(path: Path) -> list[ProductIdRange]:
    content = path.read_text(encoding="utf-8").strip()
    product_id_ranges = []
    for pair in content.split(","):
        first_id, last_id = pair.split("-")
        product_id_ranges.append(ProductIdRange(int(first_id), int(last_id)))
    return product_id_ranges


@dataclass(frozen=True)
class ProductIdRange:
    first_id: int
    last_id: int

    def __str__(self) -> str:
        return f"{self.first_id}-{self.last_id}"


if __name__ == "__main__":
    main()
