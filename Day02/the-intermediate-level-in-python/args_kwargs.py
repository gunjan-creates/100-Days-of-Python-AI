"""Explains positional and keyword argument collection in functions."""
from typing import Any


def summarize(*args: Any, **kwargs: Any) -> None:
    print("Positional args:", args)
    print("Keyword args:", kwargs)


if __name__ == "__main__":
    summarize(1, 2, 3, user="alex", active=True)
