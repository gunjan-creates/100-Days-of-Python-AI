"""Parses CSV data using the csv module."""
import csv
from io import StringIO

DATA = """name,score\nAna,92\nBo,85\nCam,78\n"""

if __name__ == "__main__":
    reader = csv.DictReader(StringIO(DATA))
    for row in reader:
        print(row)
