#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


def inherits_from(obj, a_class):
    """
    this is a inheritance class
    """
    if isinstance(obj, a_class):
        return True
    else:
        if type(obj) is not a_class:
            return False
