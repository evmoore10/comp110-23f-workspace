"""Testing dictionary!"""
__author__ = "730670009"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def invert_test_1() -> None:
    """Test keys and values."""
    test_keys_and_values: dict[str, str] = {"john": "paul"}
    assert invert(test_keys_and_values) == {"paul": "john"}


def invert_test_2() -> None:
    """Test if integer."""
    test_element: dict[str, str] = {"55": "11"}
    assert invert(test_element) == {"11": "55"}


def invert_test_3() -> None:
    """Test for empty dict!"""
    with pytest.raises(KeyError):
        dict_test: list[str] = {"Error!"}
        favorite_color(dict_test)


def favorite_color_test_1() -> None:
    """Test if correct color is outputed."""
    dict_test: dict[str, str] = {"candy": "green", "drink": "purple", "food": "green"}
    assert favorite_color(dict_test) == "green"


def favorite_color_test_2() -> None:
    """Test if only 2 colors."""
    test_colors: dict[str, str] = {"UNC": "light blue", "Duke": "dark blue"}
    assert favorite_color(test_colors) == "light blue"


def favorite_color_test_3() -> None:
    """Test if using wrong type."""
    assert favorite_color([], []) == {}


def count_test_1() -> None:
    """Check when something appears just once."""
    list_test: list[str] = {"Homework"}
    assert count(list_test) == {"Homework": 1}


def count_test_2() -> None:
    """Check when something appears twice."""
    list_test: list[str] = {"Homework", "Homework"}
    assert count(list_test) == {"Homework": 2}


def count_test_3() -> None:
    """Test if wrong element."""
    with pytest.raises(KeyError):
        dict_test: list[str] = {"Error!"}
        favorite_color(dict_test)


def alphabetizer_test_1() -> None:
    """Test when two different starting letters."""
    letter_test: list[str] = ["Comp", "Math"]
    assert alphabetizer(letter_test) == {"c": ["Comp"], "m": ["Math"]}


def alphabetizer_test_2() -> None:
    """Test when same starting letter."""
    same_letter_test: list[str] = ["Comp", "Computer"]
    assert alphabetizer(same_letter_test) == {"c": ["Comp", "Computer"]}


def alphabetizer_test_3() -> None:
    """Test if empty dict."""
    list_test: list[str] = []
    assert alphabetizer(list_test) == {}


def update_attendance_test_1() -> None:
    """Testing updated attendance."""
    dict_test: dict[str, list[str]] = {"Saturday": []}
    day: str = "Saturday"
    student: str = "Evan"
    assert update_attendance(dict_test, day, student) == {"Saturday": ["Evan"]}


def update_attendance_test_2() -> None:
    """Update attendance for student under multiple days and names."""
    dict_test: dict[str, list[str]] = {"Saturday": [], "Sunday": []}
    day: str = "Saturday", "Sunday"
    student: str = "Evan", "Moore"
    assert update_attendance(dict_test, day, student) == {"Saturday": ["Evan", "Moore"], "Sunday": ["Evan", "Moore"]}


def update_attendance_test_3() -> None:
    """Test if student attend same day again."""
    dict_test: dict[str, list[str]] = {"Saturday": ["Evan"]}
    day: str = "Saturday"
    student: str = "Evan"
    assert update_attendance(dict_test, day, student) == {"Saturday": ["Evan", "Evan"]}