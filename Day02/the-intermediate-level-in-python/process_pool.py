"""Uses ProcessPoolExecutor for CPU-bound tasks."""
from concurrent.futures import ProcessPoolExecutor


def heavy_square(number: int) -> int:
    total = 0
    for _ in range(100_000):
        total += number * number
    return total


if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(heavy_square, range(5)))
    print("Results:", results)
