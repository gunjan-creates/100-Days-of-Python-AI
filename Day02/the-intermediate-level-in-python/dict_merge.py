"""Demonstrates dictionary merging and unpacking for configuration overrides."""

DEFAULTS = {
    "timeout": 30,
    "retries": 3,
    "headers": {"Accept": "application/json"},
}

OVERRIDES = {
    "timeout": 10,
    "headers": {"User-Agent": "intermediate-demo"},
}

if __name__ == "__main__":
    merged = DEFAULTS | OVERRIDES
    merged["headers"] = {**DEFAULTS["headers"], **OVERRIDES["headers"]}
    print("Merged configuration:", merged)
