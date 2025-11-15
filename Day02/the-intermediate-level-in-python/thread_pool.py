"""Uses ThreadPoolExecutor to parallelize I/O-bound work."""
from concurrent.futures import ThreadPoolExecutor
import time


def fetch(name: str) -> str:
    time.sleep(0.1)
    return f"Fetched {name}"


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as executor:
        for result in executor.map(fetch, ["alpha", "beta", "gamma"]):
            print(result)
