"""Uses abstract base classes to define interfaces."""
from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        raise NotImplementedError


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Email: {message}")


if __name__ == "__main__":
    notifier = EmailNotifier()
    notifier.send("System maintenance at midnight")
