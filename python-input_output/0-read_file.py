#!/usr/bin/python3
"""
this is a module for interpreting python3
"""

def read_file(filename=""):
    """
    readfile encoding utf8
    """
    with open(filename, encoding="utf-8", end="") as f:
        print(filename)
        f.closed
