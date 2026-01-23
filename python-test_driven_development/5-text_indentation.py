#!/usr/bin/python3
"""
Module 5-text_indentation
This module provides a function that prints a text with two new lines
after each of these characters: '.', '?' and ':'.
"""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    buf = ""
    for ch in text:
        buf += ch
        if ch in ".?:":
            print(buf.strip(), end="")
            print("\n")
            buf = ""

    if buf.strip() != "":
        print(buf.strip(), end="")
