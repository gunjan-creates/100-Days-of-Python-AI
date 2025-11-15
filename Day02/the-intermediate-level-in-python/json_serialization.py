"""Serializes Python objects to JSON and back."""
import json
from dataclasses import asdict, dataclass


@dataclass
class User:
    name: str
    active: bool
    roles: list[str]


if __name__ == "__main__":
    user = User(name="Mira", active=True, roles=["editor", "admin"])
    payload = json.dumps(asdict(user))
    print("JSON:", payload)
    restored = json.loads(payload)
    print("Restored:", restored)
