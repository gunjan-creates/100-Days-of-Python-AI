"""Maintains a priority queue using heapq."""
import heapq

if __name__ == "__main__":
    tasks = [(3, "email"), (1, "deploy"), (2, "report")]
    heapq.heapify(tasks)
    while tasks:
        priority, name = heapq.heappop(tasks)
        print(priority, name)
