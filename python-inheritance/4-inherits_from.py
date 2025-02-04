#!/usr/bin/python3
"""
This is a module a square class
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an  instance inherits of a_class (directly or indirectly)
    """

    if isinstance(obj, a_class) or type(obj) is a_class:
        return True
