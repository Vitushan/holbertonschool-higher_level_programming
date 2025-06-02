#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


def append_write(filename="", text=""):
    """
    append write
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
