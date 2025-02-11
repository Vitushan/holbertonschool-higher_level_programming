#!/usr/bin/python3
"""
Create an Object from a Json file
"""
import json


def load_from_json_file(filename):
    """
    Create an Object from a Json file
    """
    with open(filename, 'r') as f:
        return json.load(f)
