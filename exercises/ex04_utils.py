"""List Utility Functions."""


__author__ = "730544769"


def all(a_list: list[int], number: int) -> bool:
    """All numbers are equal to other number."""
    a = 0
    while a < len(a_list):
        if a_list[a] != number:
            return False
        else:
            a += 1
    return True


def max(a_list: list[int]) -> int:
    """Returns highest number in list."""
    if len(a_list) == 0:
        raise ValueError("max() arg is an empty List")
    a = 0
    max_number = 0
    while a < len(a_list):
        if a_list[a] > max_number:
            max_number == a_list[a]
            a += 1
        else:
            a += 1
    return max_number


def is_equal(a_list: list[int], b_list: list[int]) -> bool:
    """If two lists equal eachother."""
    if a_list == b_list:
        return True
    else:
        return False


def extend(a_list: list[int], b_list: list[int]) -> None:
    """Appending second list values to end of first list."""
    a = 0
    while a < len(b_list): 
        a_list.append(b_list[a])
        a += 1
