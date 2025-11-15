"""Illustrates generator usage for memory-efficient data processing."""
from typing import Iterable, Iterator, Tuple


def squared_values(numbers: Iterable[int]) -> Iterator[int]:
    """Yields the square of each number lazily."""
    for number in numbers:
        yield number * number


def running_average(numbers: Iterable[int]) -> Iterator[Tuple[int, float]]:
    """Produces the running average after each new value."""
    total = 0
    count = 0
    for number in numbers:
        count += 1
        total += number
        yield count, total / count


def demo_generator_chain(limit: int = 10) -> None:
    """Prints squared values alongside their running averages."""
    numbers = range(1, limit + 1)
    for (index, average), squared in zip(running_average(numbers), squared_values(numbers)):
        print(f"after {index:>2} numbers, squared={squared:>3}, average={average:>5.2f}")


if __name__ == "__main__":
    demo_generator_chain()
