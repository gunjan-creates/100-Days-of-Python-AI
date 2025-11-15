"""Stores and loads Python objects using pickle."""
import pickle
from pathlib import Path

PATH = Path("session.pkl")

if __name__ == "__main__":
    session = {"token": "abc123", "expires_in": 3600}
    PATH.write_bytes(pickle.dumps(session))
    loaded = pickle.loads(PATH.read_bytes())
    print("Loaded session:", loaded)
