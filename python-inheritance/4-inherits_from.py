#!/usr/bin/python3
"""
This is a module a  obj class
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an  instance of a class that inherited from a_class
    """

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
