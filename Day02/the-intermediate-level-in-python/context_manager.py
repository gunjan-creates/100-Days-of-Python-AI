"""Shows how to create a custom context manager for temporary configuration."""
from contextlib import contextmanager
from typing import Iterator

CONFIG = {
    "theme": "light",
    "language": "en",
}


@contextmanager
def temporary_config(key: str, value: str) -> Iterator[None]:
    """Temporarily overrides a configuration key within a with-block."""
    original = CONFIG.get(key)
    CONFIG[key] = value
    try:
        yield
    finally:
        if original is None:
            CONFIG.pop(key, None)
        else:
            CONFIG[key] = original


def describe_config() -> None:
    """Prints the current configuration map."""
    print("Current configuration:")
    for name, value in CONFIG.items():
        print(f"  {name}: {value}")


if __name__ == "__main__":
    describe_config()
    with temporary_config("theme", "dark"):
        print("\nInside context manager:")
        describe_config()
    print("\nAfter context manager:")
    describe_config()
