"""Simplifies grouping with collections.defaultdict."""
from collections import defaultdict

if __name__ == "__main__":
    students = [
        ("Ana", "math"),
        ("Ana", "physics"),
        ("Bo", "math"),
        ("Cam", "history"),
    ]

    courses: defaultdict[str, list[str]] = defaultdict(list)
    for name, course in students:
        courses[name].append(course)

    for name, course_list in courses.items():
        print(name, "->", course_list)
