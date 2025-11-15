"""Uses contextlib.closing to ensure resources close properly."""
from contextlib import closing
from urllib.request import urlopen

URL = "https://www.example.com"

if __name__ == "__main__":
    with closing(urlopen(URL)) as response:
        print("Status:", response.status)
        print("Headers lines:", len(response.headers))
