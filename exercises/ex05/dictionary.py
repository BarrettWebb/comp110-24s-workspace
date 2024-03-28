"""Dictonary."""

___author___ = "730544769"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the keys and the values."""
    invert_dict = {}
    for key in dictionary:
        if dictionary[key] in invert_dict:
            raise ValueError("Invalid input!")
        value = dictionary[key]
        invert_dict[value] = key
    return invert_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Return most used color."""
    colors_said: dict[str, int] = {}
    count = 0
    favorite: str = ""
    for key in colors:
        color = colors[key]
        if color in colors_said:
            colors_said[color] += 1
        else:
            colors_said[color] = 1

        if colors_said[color] > count:
            count = colors_said[color]
            favorite = color
    return favorite


def count(input: list[str]) -> dict[str, int]:
    """Count number of times value was given."""
    count: dict[str, int] = {}
    for idx in input:
        if idx in count:
            count[idx] += 1
        else:
            count[idx] = 1
    return count


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Alphabetize list."""
    alphabetized: dict[str, list[str]] = {}
    for idx in input:
        first_letter = idx[0]
        if first_letter not in alphabetized:
            alphabetized[first_letter] = []
        alphabetized[first_letter].append(idx)
    return alphabetized


def update_attendance(attendance: dict[str, list[str]], day: str, name: str) -> None:
    """Mutate and return attendance."""
    if day in attendance:
        attendance[day].append(name)
    else:
        attendance[day] = [name]
    return None