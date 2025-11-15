"""Shows computed attributes using the @property decorator."""


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height


if __name__ == "__main__":
    rect = Rectangle(4, 5)
    print("Area:", rect.area)
