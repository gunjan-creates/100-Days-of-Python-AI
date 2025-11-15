"""Showcases collections.namedtuple for lightweight structures."""
from collections import namedtuple

Point = namedtuple("Point", "x y")

if __name__ == "__main__":
    point = Point(3, 4)
    print(point)
    print("As tuple:", tuple(point))
