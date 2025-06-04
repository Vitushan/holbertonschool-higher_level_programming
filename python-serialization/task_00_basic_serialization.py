#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


import pickle, json

def serialize_and_save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        json.load(f)
