#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


def class_to_json(obj):
    """
    return dictionary description
    """
    return obj.__dict__
