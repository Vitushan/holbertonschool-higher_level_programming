#!/usr/bin/python3
"""
Return the dictionary description
"""


def class_to_json(obj):
    """
    return dictionary of item fo the serializing JSON
    """
    return obj.__dict__
