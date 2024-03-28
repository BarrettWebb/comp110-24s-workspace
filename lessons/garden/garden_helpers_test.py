"""Test my garden functions."""


__author__ = "730544769"


from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_empty() -> None:
    """Test empty plant dict."""
    garden_dict = {}
    assert add_by_kind(garden_dict, "flower", "lilly") == {"flower", "lilly"}


def test_add_by_kind_full():
    """Add onto dict."""
    garden_dict = {"flower": ["rose", "lilly", "lavender"], "vegetable": ["carrots"], "fruit": ["apple"]}
    assert add_by_kind(garden_dict, "flower", "daisy") == {"flower": ["rose", "lilly", "lavender", "daisy"], "vegetable": ["carrots"], "fruit": ["apple"]}
    

def test_add_by_date_empty() -> None:
    """Add empty date dict."""
    garden_dict = {}
    assert add_by_date(garden_dict, "August", "rose") == {"August", "rose"}


def test_add_by_date_full() -> None:
    """Add to full dict."""
    garden_dict = {"August": ["rose", "lilly"], "May": ["lavender"]}
    assert add_by_date(garden_dict, "July", "daisy") == {"August": ["rose", "lilly"], "May": ["lavender"], "July": ["daisy"]}


def test_lookup_by_kind_and_date_empty() -> None:
    """Test empty dict."""
    by_kind = {"flower": ["rose", "daisy"], "vegetable": ["carrot"]}
    by_date = {}
    assert lookup_by_kind_and_date(by_kind, by_date, "flower", "August") == "No flowers to plant in August."


def test_lookup_by_kind_and_date_full() -> None:
    """Test full dict."""
    by_kind = {"flower": ["rose", "daisy"], "vegetable": ["carrot"]}
    by_date = {"August": ["rose", "lilly"], "May": ["lavender"]}
    assert lookup_by_kind_and_date(by_kind, by_date, "flower", "August")