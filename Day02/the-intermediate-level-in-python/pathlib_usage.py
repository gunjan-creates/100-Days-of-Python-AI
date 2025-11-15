"""Demonstrates pathlib for filesystem navigation and filtering."""
from pathlib import Path

if __name__ == "__main__":
    current = Path.cwd()
    python_files = list(current.glob("*.py"))
    print("Current directory:", current)
    print("Python files:")
    for path in python_files:
        print(" -", path.name)
