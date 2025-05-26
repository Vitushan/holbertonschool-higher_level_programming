#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


def inherits_from(obj, a_class):
    """
    this is a inheritance class
    """
    if a_class(obj) is obj:
        return True
    return False
