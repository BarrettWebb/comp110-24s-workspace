"""Lesson on recursion."""


__author__ = "730544769"


def f(n: int, k: int) -> int:
    """Multiply values together."""
    if n == 0:
        return 0
    else:
        return f(n - 1, k) + k
