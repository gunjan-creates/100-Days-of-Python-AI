"""Uses regular expressions to validate and extract email usernames."""
import re

EMAIL_PATTERN = re.compile(r"^(?P<user>[\w.-]+)@(?P<domain>[\w.-]+)$")

if __name__ == "__main__":
    addresses = ["alex@example.com", "bad-email", "sam@company.org"]
    for address in addresses:
        match = EMAIL_PATTERN.match(address)
        if match:
            print(f"{address} -> user={match.group('user')}, domain={match.group('domain')}")
        else:
            print(f"Invalid email: {address}")
