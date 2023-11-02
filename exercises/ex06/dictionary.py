"""Practice with Dictionarys!"""

__author__ = "730670009"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts keys and the values."""
    new_dict: dict[str, str] = {}
    for x in dict1:
        new_dict[dict1[x]] = x
    return new_dict


def favorite_color(dict1: dict[str, str]) -> str:
    """Return the most frequent color."""
    color_dict: dict[str, int] = {}
    for colors in dict1:
        if colors in color_dict:
            color_dict[colors] += 1
        else:
            color_dict[colors] = 1
    main_color: str = ""
    value: int = 0
    for colors in color_dict:
        if color_dict[colors] > value:
            value = color_dict[colors]
            main_color = colors
    return main_color
    

def count(list1: list[str]) -> dict[str, int]:
    """Returns a dictionary of the counts of items in input list."""
    new_dict: dict[str, int] = {}
    for x in list1:
        if x in new_dict:
            new_dict[x] += 1
        else:
            new_dict[x] = 1
    return new_dict


def alphabitizer(list1: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary of letters and words that belong to the letter."""
    new_dict: dict[str, list[str]] = {}
    for x in list1:
        lowercase_x = x.lower()
        if x[0] in new_dict:
            new_dict[lowercase_x[0]] += x
        else:
            new_dict[lowercase_x[0]] = x
    return new_dict


def update_attendance(dict1: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Check if student attended class."""
    if day in dict1:
        dict1[day] += [student]
    else:
        dict1[day] = [student]
    return dict1