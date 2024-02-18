"""Mutating functions."""

__author__ = "730544769"


def manual_append(appending: list[int], append: int) -> None:
    """Mutate input."""
    appending.append(append)


def double(a_list: list[int]) -> None:
    """Double input."""
    a = 0
    while a < len(a_list):
        a_list[a] = (a_list[a] * 2)
        a += 1