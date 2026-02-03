#!/usr/bin/python3
"""Returns True if object is an instance otherwise False."""


def is_same_class(obj, a_class):
    """Return True if obj is  an instance of a_class, otherwise False."""
    if type(obj) is a_class:
        return True
    else:
        return False
