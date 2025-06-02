#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


def write_file(filename="", text=""):
    """
    write file with encoding utf8
    """
    with open(filename, encoding='utf-8') as f:
        f = f.read(), end=""
        return f
