#!/usr/bin/bash/python3
"""
;;;:
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    ...
    """
    with open(filename, 'w', encoding="utf-8"):
        return json.dumps(filename, data)


def load_and_deserialize(filename):
    """
    ...
    """
    return json.loads(filename)
