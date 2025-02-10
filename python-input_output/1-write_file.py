#!/usr/bin/python3
"""
this is a module for write in the file
"""


def write_file(filename="", text=""):
    """
    for write ont the file in utf-8 encoding
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
