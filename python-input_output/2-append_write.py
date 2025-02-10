#!/usr/bin/python3
"""
...
"""


def append_write(filename="", text=""):
    """
    append a string end returns the number of characters
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.append(text)
