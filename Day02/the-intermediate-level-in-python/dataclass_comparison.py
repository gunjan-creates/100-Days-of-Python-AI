"""Uses dataclass ordering to support comparisons."""
from dataclasses import dataclass


@dataclass(order=True)
class Task:
    priority: int
    name: str


if __name__ == "__main__":
    tasks = [Task(2, "email"), Task(1, "deploy"), Task(3, "backup")]
    for task in sorted(tasks):
        print(task)
