"""Practice writing a class."""
from __future__ import annotations


__author__ = "730544769"


class Point: 
    """Points class."""

    x: float
    y: float

    def __init__(self, x_input: float, y_input: float):
        """Create new point."""
        self.x = x_input
        self.y = y_input

    def scale_by(self, factor: int) -> None:
        """Scale point by amount."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Add new scaled point."""
        return Point(self.x * factor, self.y * factor)