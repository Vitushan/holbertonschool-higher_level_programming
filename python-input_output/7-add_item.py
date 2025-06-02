#!/usr/bin/python3
"""
this is a module for interpreting python3
"""

import json
import sys



save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').save_to_json_file
f = 'add_item.json'

with open(save_to_json_file, 'r', encoding='utf-8') and open(load_from_json_file) as f:
    json.load(f)

add_item = []
add_item.append(save_to_json_file, load_from_json_file)
print(add_item)
