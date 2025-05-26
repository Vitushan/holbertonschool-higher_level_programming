#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


def inherits_from(obj, a_class):
    """
    this is a inheritance class
    """
    if all(isinstance(obj, a_class)):
        return True
    return False
