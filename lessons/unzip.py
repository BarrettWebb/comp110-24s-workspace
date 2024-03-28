"""Splitting a dictionary into two lists."""

__author__ = "730544769"


def get_keys(dict1: dict[str, int]) -> list[str]:
    """Return list of keys."""
    list1: list[str] = []
    for key in dict1:
        list1.append(key)
    return list1


def get_values(dict2: dict[str, int]) -> list[int]:
    """Return list of values."""
    list2: list[int] = []
    for key in dict2:
        list2.append(dict2[key])
    return list2