"""Builds a simple CLI using argparse."""
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Greeting CLI")
    parser.add_argument("name", help="Name to greet")
    parser.add_argument("--caps", action="store_true", help="Use uppercase output")
    args = parser.parse_args()
    message = f"Hello, {args.name}!"
    if args.caps:
        message = message.upper()
    print(message)
