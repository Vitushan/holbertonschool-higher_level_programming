#!/usr/bin/python3
"""
Module that defines True is the object is instance
"""


def is_same_class(obj, a_class):
    if isinstance(obj, object) or isinstance(a_class, object):
        return True
    else:
        return False