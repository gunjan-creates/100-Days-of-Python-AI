"""Uses bisect to maintain a sorted list."""
import bisect

if __name__ == "__main__":
    scores = [20, 40, 60, 80]
    bisect.insort(scores, 50)
    bisect.insort(scores, 90)
    print("Sorted scores:", scores)
