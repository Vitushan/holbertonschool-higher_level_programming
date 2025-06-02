#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


import json


def save_to_json_file(my_obj, filename):
    """
     function that writes an
     Object to a text file,
     using a JSON representation
    """
    return json.load(filename, my_obj)
