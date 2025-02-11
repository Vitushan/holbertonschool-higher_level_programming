#!/usr/bin/python3
"""
append a string end returns the number of characters
"""


def append_write(filename="", text=""):
    """
    append a string end returns the number of characters
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
