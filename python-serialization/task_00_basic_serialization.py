#!/usr/bin/python3
"""
this module serialize data and save to the file
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    serialize data and save to the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    load data from a file and deserialize it
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
