"""Demonstrates creating and using decorators, including passing arguments to them."""
from functools import wraps
from time import perf_counter


def log_execution(prefix: str = "LOG"):
    """Decorator factory that logs the execution time of a function."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = perf_counter()
            result = func(*args, **kwargs)
            duration = (perf_counter() - start) * 1000
            print(f"{prefix}: {func.__name__} took {duration:.2f} ms")
            return result

        return wrapper

    return decorator


@log_execution(prefix="DEBUG")
def fibonacci(n: int) -> int:
    """Computes the n-th Fibonacci number using iteration."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    for number in range(10):
        value = fibonacci(number)
        print(f"fibonacci({number}) = {value}")
