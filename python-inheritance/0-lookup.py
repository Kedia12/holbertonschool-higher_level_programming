#!/usr/bin/python3
"""A function that lists an object's available attributes and methods."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
