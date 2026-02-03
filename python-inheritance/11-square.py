#!/usr/bin/python3
"""Define Square, a subclass of Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with a validated private size."""

    def __init__(self, size):
        """Initialize a square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the string form: [Square] <width>/<height>."""
        return f"[Square] {self.__size}/{self.__size}"
