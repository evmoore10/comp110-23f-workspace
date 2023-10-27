"""Test my zip function"""

__author__ = "730670009"

from lessons.zip import zip


def test_coresponding_elements() -> None:
    """Testing string and integer!"""
    test_values: list[int] = [2]
    test_keys: list[str] = ["Happy"]
    assert zip(test_keys, test_values) == {"Happy": 2}


def test_birthday() -> None:
    """Test another string and integer!"""
    test_values: list[int] = [3]
    test_keys: list[str] = ["Birthday"]
    assert zip(test_keys, test_values) == {"Birthday": 3}


def test_wrong_length() -> None:
    """Test for empty list"""
    assert zip([], []) == {}