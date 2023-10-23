"""Writing the same function in 3 ways!"""

__author__ = "730670009"


def w_sum(vals: list[float]) -> float:
    """Calculate sum with while loop!"""
    sum: float = 0.0
    idx: int = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Calculate sum with for loop!"""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Calculate sum with range!"""
    sum: float = 0.0
    for elem in range(0, len(vals)):
        sum += vals[elem]
    return sum
