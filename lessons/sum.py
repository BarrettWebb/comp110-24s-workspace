"""Summing the elements of a list using different loops."""


__author__ = "730544769"


def w_sum(val1: list[float]) -> float:
    """Sum with while."""
    sum = float()
    number: int = 0

    while number < len(val1):
        sum += val1[number]
        number += 1
    return sum


def f_sum(val1: list[float]) -> float:
    """Sum with for."""
    sum = float()
    for number in val1:
        sum += number
    return sum


def f_range_sum(val1: list[float]) -> float:
    """Sum with for range."""
    sum = float()
    for number in range(len(val1)):
        sum += val1[number]
    return sum