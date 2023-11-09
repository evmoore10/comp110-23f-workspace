"""Testing dictionary!"""
__author__ = "730670009"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_1() -> None:
    """Test keys and values."""
    test_keys_and_values: dict[str, str] = {"john": "paul"}
    assert invert(test_keys_and_values) == {"paul": "john"}


def test_invert_2() -> None:
    """Test if integer."""
    test_element: dict[str, str] = {"55": "11"}
    assert invert(test_element) == {"11": "55"}


def test_invert_3() -> None:
    """Test for wrong key."""
    with pytest.raises(KeyError):
        test_list: dict[str, str] = {"10": "15", "1": "15"}
        invert(test_list)


def test_favorite_color_1() -> None:
    """Test if correct color is outputed."""
    dict_test: dict[str, str] = {"candy": "green", "drink": "purple", "food": "green"}
    assert favorite_color(dict_test) == "green"


def test_favorite_color_2() -> None:
    """Test if only 2 colors."""
    test_colors: dict[str, str] = {"UNC": "light blue", "Duke": "dark blue"}
    assert favorite_color(test_colors) == "light blue"


def test_favorite_color_3() -> None:
    """Empty."""
    dict_test: dict[str, str] = []
    assert favorite_color(dict_test) == ""


def test_count_1() -> None:
    """Check when something appears just once."""
    list_test: list[str] = ["Homework"]
    assert count(list_test) == {"Homework": 1}


def test_count_2() -> None:
    """Check when something appears twice."""
    list_test: list[str] = ["Homework", "Homework"]
    assert count(list_test) == {"Homework": 2}


def test_count_3() -> None:
    """Test if wrong element."""
    with pytest.raises(TypeError):
        dict_test: dict[str, str] = {"Error!": "2"}
        count(dict_test)


def test_alphabetizer_1() -> None:
    """Test when two different starting letters."""
    letter_test: list[str] = ["Comp", "Math"]
    assert alphabetizer(letter_test) == {'c': ["Comp"], 'm': ["Math"]}


def test_alphabetizer_2() -> None:
    """Test when same starting letter."""
    same_letter_test: list[str] = ["Comp", "computer"]
    assert alphabetizer(same_letter_test) == {'c': ["Comp", "computer"]}


def test_alphabetizer_3() -> None:
    """Test if empty dict."""
    list_test: list[str] = []
    assert alphabetizer(list_test) == {}


def test_update_attendance_1() -> None:
    """Testing updated attendance."""
    dict_test: dict[str, list[str]] = {"Saturday": []}
    day: str = "Saturday"
    student: str = "Evan"
    assert update_attendance(dict_test, day, student) == {"Saturday": ["Evan"]}


def test_update_attendance_2() -> None:
    """Update attendance for student under multiple days and names."""
    dict_test: dict[str, list[str]] = {"Saturday": ["Evan"], "Sunday": []}
    day: str = "Saturday"
    student: str = "Moore"
    assert update_attendance(dict_test, day, student) == {"Saturday": ["Evan", "Moore"], "Sunday": []}


def test_update_attendance_3() -> None:
    """Test if student attend same day again."""
    dict_test: dict[str, list[str]] = {'Saturday': ['Evan']}
    day: str = "Saturday"
    student: str = "Evan"
    assert update_attendance(dict_test, day, student) == {"Saturday": ['Evan', 'Evan']}