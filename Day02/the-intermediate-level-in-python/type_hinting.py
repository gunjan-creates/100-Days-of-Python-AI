"""Highlights type hints and static typing benefits."""
from typing import Iterable


def total_length(items: Iterable[str]) -> int:
    return sum(len(item) for item in items)


if __name__ == "__main__":
    length = total_length(["alpha", "beta", "gamma"])
    print("Total length:", length)
