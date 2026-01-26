#!/usr/bin/python3
"""Defines a Square class with a private instance attribute."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a Square with a private size attribute."""
        self.__size = size
