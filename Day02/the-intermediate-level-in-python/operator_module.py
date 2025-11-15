"""Uses the operator module for readable arithmetic and attribute access."""
from operator import attrgetter, itemgetter, mul


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


if __name__ == "__main__":
    values = [1, 2, 3, 4]
    result = mul(5, 6)
    second_item = itemgetter(1)(values)
    products = [Product("Pen", 1.5), Product("Notebook", 3.0)]
    cheapest = min(products, key=attrgetter("price"))

    print("Multiplication:", result)
    print("Second item:", second_item)
    print("Cheapest product:", cheapest.name)
