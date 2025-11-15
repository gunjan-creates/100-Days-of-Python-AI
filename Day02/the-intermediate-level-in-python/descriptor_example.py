"""Implements a descriptor to enforce positive values."""


class Positive:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.public_name} must be positive")
        setattr(instance, self.private_name, value)


class Account:
    balance = Positive()

    def __init__(self, balance: float) -> None:
        self.balance = balance


if __name__ == "__main__":
    account = Account(100)
    print("Balance:", account.balance)
    try:
        account.balance = -10
    except ValueError as error:
        print("Error:", error)
