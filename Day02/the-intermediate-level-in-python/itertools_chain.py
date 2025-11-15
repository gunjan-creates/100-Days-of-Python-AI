"""Combines multiple iterables seamlessly using itertools utilities."""
from itertools import chain, cycle, islice

if __name__ == "__main__":
    combined = chain(range(3), "abc", [True, False])
    print("Chained items:", list(combined))

    cycled = list(islice(cycle("PY"), 10))
    print("Cycled slice:", cycled)
