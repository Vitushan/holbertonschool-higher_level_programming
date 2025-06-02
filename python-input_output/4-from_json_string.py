#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


import json


def from_json_string(my_str):
    """
     function that returns an object
     (Python data structure)
     represented by a JSON string
    """
    with open(my_str, 'w', encoding='utf-8') as f:
        return json.loads(my_str)
