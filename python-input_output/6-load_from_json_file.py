#!/usr/bin/python3
"""
...
"""
import json


def load_from_json_file(filename):
    """
    ...
    """
    with open(filename, 'w') as f:
        json.dump(filename.json)
        return filename
