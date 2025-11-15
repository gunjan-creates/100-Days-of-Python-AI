"""Shows advanced list comprehension patterns including conditionals and nested loops."""

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]

if __name__ == "__main__":
    squares = [n * n for n in range(1, 11)]
    odds = [n for n in range(1, 21) if n % 2]
    prime_pairs = [(a, b) for a in PRIMES for b in PRIMES if a < b and a + b < 25]

    print("Squares:", squares)
    print("Odds:", odds)
    print("Prime pairs with sum<25:", prime_pairs)
