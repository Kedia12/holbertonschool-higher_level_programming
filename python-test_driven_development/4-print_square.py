#!/usr/bin/python3
"""
Module 4-print_square
This module provides a function that prints a square using the '#'
character. The size is validated and the square is printed to stdout.
"""


def print_square(size):
    """Print a square of size `size` using the '#' character."""
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
