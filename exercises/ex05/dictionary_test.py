"""Testing dictionary."""


__author__ = "730544769"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance 


def test_invert_empty() -> None:
    """Test empty invert."""
    invert_dict = {}
    return invert(invert_dict) == {}


def test_invert_full() -> None:
    """Test proper invert."""
    invert_dict = {'x': 'y', 'a': 'b'}
    assert invert(invert_dict) == {'y': 'x', 'b': 'a'}


def test_invert_again() -> None:
    """Test second use case."""
    invert_dict = {'y': 'z', 'c': 'f'}
    assert invert(invert_dict) == {'z': 'y', 'f': 'c'}


def test_favorite_color_empty() -> None:
    """Test empty dict."""
    colors = {}
    assert favorite_color(colors) == {}


def test_favorite_color_full() -> None:
    """Test proper favorite color."""
    colors = {"Barrett": "blue", "John": "green", "Kris": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_again() -> None:
    """Test second use case."""
    colors = {'greg': 'red', 'tim': 'green', 'sarah': 'red'}
    assert favorite_color(colors) == 'red'


def test_count_empty() -> None:
    """Test empty count."""
    input = {}
    assert count(input) == {}


def test_count_full() -> None:
    """Test proper count."""
    input = {'black', 'grey', 'black', 'blue'}
    assert count(input) == {'black': 2, 'grey': 1, 'blue': 1}


def test_count_again() -> None:
    """Test second use case."""
    input = {'grey', 'purple', 'grey', 'white'}
    assert count(input) == {'grey': 2, 'purple': 1, 'white': 1}


def test_alphabetizer_empty() -> None:
    """Test empty alphabetizer."""
    input = {}
    assert alphabetizer(input) == {}


def test_alphabetizer_full() -> None:
    """Test proper alphabetizer."""
    input = {'Barrett', 'blue', 'Grey', 'Cap', 'Goose'}
    assert alphabetizer(input) == {'B': ['Barrett', 'Blue'], 'G': ['Grey', 'Goose'], 'C': ['Cap']}


def test_alphabetizer_again() -> None:
    """Test second use case."""
    input = {'Rainbow', 'Cake', 'Crow'}
    assert alphabetizer(input) == {'R': ["Rainbow"], 'C': ['Cake', 'Crow']}


def test_update_attendance_empty() -> None:
    """Test update attendance empty."""
    attendance = {}
    assert update_attendance(attendance, '', '') == {}


def test_update_attendance_full() -> None:
    """Test proper update attendance."""
    attendance = {'Monday': ['Barrett', "Chris"], 'Tuesday': ['Emma']}
    assert update_attendance(attendance, 'Tuesday', 'Greg') == {'Monday': ['Barrett', "Chris"], 'Tuesday': ['Emma', 'Greg']}


def test_update_attendance_again() -> None:
    """Test second use case."""
    attendance = {'Tuesday': ['Tim', 'Brandy'], 'Friday': ['Jordan']}
    assert update_attendance(attendance, 'Friday', 'Jordan') == {'Tuesday': ['Tim', 'Brandy'], 'Friday': ['Jordan']}