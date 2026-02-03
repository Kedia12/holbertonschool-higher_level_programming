#!/usr/bin/python3
"""A function to check instance or inherited instance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
