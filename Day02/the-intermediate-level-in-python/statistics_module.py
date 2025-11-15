"""Computes descriptive statistics using the statistics module."""
import statistics as stats

DATA = [12, 15, 21, 18, 16, 15, 17]

if __name__ == "__main__":
    print("Mean:", stats.mean(DATA))
    print("Median:", stats.median(DATA))
    print("Variance:", stats.pvariance(DATA))
