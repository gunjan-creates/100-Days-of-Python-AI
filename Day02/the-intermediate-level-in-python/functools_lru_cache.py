"""Demonstrates caching expensive function calls with lru_cache."""
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for i in range(10):
        print(i, fibonacci(i))
    print("Cache info:", fibonacci.cache_info())
