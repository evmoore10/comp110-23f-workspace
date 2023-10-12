"""Using utils!"""

__author__ = "730670009"


def all(list: list[int], given_int: int) -> bool:
    """Determine if all the numbers in a list are the same as given number."""
    check: bool = True
    index: int = 0
    while index < len(list):
        if list[index] != given_int:
            check = False
            return check
        index += 1
    return check


def max(input: list[int]) -> int:
    """Find max number in a given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    indx: int = 0
    big: int = input[0]
    while indx < len(input):
        if input[indx] > big:
            big = input[indx]
        indx += 1
    return big

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determine if both lists are identical."""
    index: int = 0
    if len(list_1) != len(list_2):
        return False
    while index < len(list_1) and len(list_2):
        if list_1[index] != list_2[index]:
            return False
        index += 1
    return True