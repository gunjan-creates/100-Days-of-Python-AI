"""Demonstrates parallel iteration with zip and handling uneven lengths."""
from itertools import zip_longest

names = ["Ana", "Bo", "Cam", "Dee"]
scores = [95, 87, 90]

if __name__ == "__main__":
    paired = list(zip(names, scores))
    print("Paired (truncated):", paired)

    padded = list(zip_longest(names, scores, fillvalue="N/A"))
    print("Paired (padded):", padded)
