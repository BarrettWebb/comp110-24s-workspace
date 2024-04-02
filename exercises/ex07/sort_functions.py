"""Functions that implement sorting algorithms."""

__author__ = ""


def insertion_sort(x: list[int]) -> list[int]:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    for idx in range(1, len(x)):
        elm = x[idx]
        unsorted = idx
        while unsorted > 0 and x[unsorted - 1] > elm:
            temp = x[unsorted]
            x[unsorted] = x[unsorted - 1]
            x[unsorted - 1] = temp
            unsorted -= 1
    return x


def selection_sort(x: list[int]) -> list[int]:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    for idx in range(len(x)):
        min_idx = idx
        for a in range(idx + 1, len(x)):
            if x[a] < x[min_idx]:
                min_idx = a
        temp = x[min_idx]
        x[min_idx] = x[idx]
        x[idx] = temp
    return x   