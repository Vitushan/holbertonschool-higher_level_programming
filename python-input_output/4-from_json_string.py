#!/usr/bin/python3
"""
Return an object data structure python represented by a JSON str
"""


import json


def from_json_string(my_str):
    """
    Return an object data structure python represented by a JSON str
    """
    return json.loads(my_str)
