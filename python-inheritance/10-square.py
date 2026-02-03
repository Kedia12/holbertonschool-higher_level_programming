#!/usr/bin/python3
"""Define Square, a subclass of Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with validated private size."""

    def __init__(self, size):
        """Initialize a Square with validated size."""
        self.integer_validator("size", size)
        self.size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
