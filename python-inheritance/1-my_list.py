#!/usr/bin/python3
"""Defines MyList, a list subclass with a sorted print method."""


class MyList(list):
    """A subclass that can print its elements sorted in ascending order."""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original."""
        print(sorted(self))
