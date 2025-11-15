"""Uses the fractions module for exact rational arithmetic."""
from fractions import Fraction

if __name__ == "__main__":
    third = Fraction(1, 3)
    sixth = Fraction(1, 6)
    total = third + sixth
    print("Total:", total)
    print("As float:", float(total))
