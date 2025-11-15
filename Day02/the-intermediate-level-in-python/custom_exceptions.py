"""Defines and handles a custom exception for business logic errors."""


class CapacityExceededError(Exception):
    """Raised when registrations would exceed capacity."""


def register(attendees: int, capacity: int) -> None:
    if attendees > capacity:
        raise CapacityExceededError(f"Cannot add {attendees} when capacity is {capacity}")
    print("Registration successful")


if __name__ == "__main__":
    try:
        register(attendees=120, capacity=100)
    except CapacityExceededError as error:
        print("Registration failed:", error)
