"""Counts items using collections.Counter."""
from collections import Counter

if __name__ == "__main__":
    words = "the quick brown fox jumps over the lazy dog".split()
    counts = Counter(words)
    print("Most common:", counts.most_common(3))
