#!/usr/bin/python3
"""Defines a Square class with a private size attribute and properties."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a Square and set the initial size."""
        self.size = size  # uses the setter for validation

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, with type and value validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
