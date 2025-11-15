"""Uses functools.partial to preset function arguments."""
from functools import partial


def power(base: int, exponent: int) -> int:
    return base ** exponent


if __name__ == "__main__":
    square = partial(power, exponent=2)
    cube = partial(power, exponent=3)
    print("Square of 4:", square(4))
    print("Cube of 3:", cube(3))
