"""Uses deque for efficient queue operations."""
from collections import deque

if __name__ == "__main__":
    queue = deque(["task1", "task2"])
    queue.append("task3")
    queue.appendleft("urgent")
    print("Queue state:", queue)
    queue.popleft()
    print("After handling urgent:", queue)
