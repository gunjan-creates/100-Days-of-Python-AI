"""Explores sorting complex data structures using lambda expressions."""
from operator import itemgetter

STUDENTS = [
    {"name": "Ava", "score": 88, "age": 20},
    {"name": "Ben", "score": 95, "age": 19},
    {"name": "Chloe", "score": 95, "age": 21},
    {"name": "Diego", "score": 72, "age": 20},
]

if __name__ == "__main__":
    by_score_then_age = sorted(STUDENTS, key=lambda s: (-s["score"], s["age"]))
    by_name = sorted(STUDENTS, key=itemgetter("name"))

    print("By score then age:")
    for student in by_score_then_age:
        print(student)

    print("\nBy name:")
    for student in by_name:
        print(student)
