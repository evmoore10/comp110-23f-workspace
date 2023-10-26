"""Combining two lists into a dictionary!"""

__author__ = "730670009"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Assigning two lists to return a dictionary!"""
    zips: dict[str, int] = {}
    
    if len(keys) != len(values):
        return zips
    
    idx: int = 0
    while idx < len(keys):
        zips[keys[idx]] = values[idx]
        idx += 1   
    return zips