#!/usr/bin/python3
"""3-say_my_name module.

This module provides say_my_name(first_name, last_name="").
It prints: My name is <first_name> <last_name>
No modules are imported.
"""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first_name> <last_name>'."""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
