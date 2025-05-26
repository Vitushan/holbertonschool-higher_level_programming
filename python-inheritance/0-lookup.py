#!/usr/bin/python3
"""
Module that defines the lookup function.
"""


def lookup(obj):
    """
    Returns the list of an object.
    args: obj
    return: list of obj
    """
    if isinstance(obj, list):
        return obj
