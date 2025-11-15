"""Introduces dataclasses for concise data containers."""
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float


if __name__ == "__main__":
    book = Book(title="Python Journeys", author="Quinn", pages=320, price=24.5)
    print(book)
