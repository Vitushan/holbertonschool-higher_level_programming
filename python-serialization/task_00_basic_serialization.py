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
        json.dumps(filename)


def load_and_deserialize(filename):
    """
    ...
    """
    json.loads(filename)
