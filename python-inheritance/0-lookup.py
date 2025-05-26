#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


def lookup(obj):
    """
    this a class
    """
    if isinstance(obj, list):
        return  dir(obj)
    else:
        for _ in range(obj):
            print(obj)
