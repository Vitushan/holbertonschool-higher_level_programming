#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


import pickle, json

def serialize_and_save_to_file(data, filename):
    with open(data, filename, 'rb', encoding='utf-8') as f:
        json.dump(f)

def load_and_deserialize(filename):
    with open(filename, 'rb', encoding='utf-8') as f:
        json.load(f)
