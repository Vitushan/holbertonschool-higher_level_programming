#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


def read_file(filename=""):
    """
    readfile encoding utf8
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
