#!/usr/bin/python3
"""0-add_integer module.

This module provides add_integer(a, b=98).
It returns the integer sum of a and b.
No modules are imported.
"""


def add_integer(a, b=98):
    """Add two numbers.

    Returns the addition of a and b as an integer.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
