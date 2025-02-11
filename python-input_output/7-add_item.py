#!/usr/bin/python3
"""
Script add all arg on the list
"""
import sys
import json
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        item = json.load(f)
else:
    item = []

item.extend(sys.argv[1:])

with open(filename, "w") as file:
    json.dump(item, file)
