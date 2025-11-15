"""Performs decimal arithmetic with controlled precision."""
from decimal import Decimal, getcontext

if __name__ == "__main__":
    getcontext().prec = 6
    price = Decimal("19.99")
    tax_rate = Decimal("0.075")
    total = price + (price * tax_rate)
    print("Total with tax:", total)
