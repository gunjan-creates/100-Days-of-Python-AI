"""Reads and writes files safely using context managers."""
from pathlib import Path

DATA_FILE = Path("demo_data.txt")

if __name__ == "__main__":
    DATA_FILE.write_text("First line\nSecond line\n", encoding="utf-8")

    with DATA_FILE.open(encoding="utf-8") as handle:
        for line in handle:
            print(line.strip())
