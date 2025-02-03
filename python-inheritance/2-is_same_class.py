#!/usr/bin/python3
"""
This is a module a obj class
"""


def is_same_class(obj, a_class):
    """
    Check if object is exactly an instance of the specified class.
    """

    return type(obj) is a_class
