#!/usr/bin/python3
"""
this is a module for interpreting python3
"""

import json
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_to_json_file


file = 'add_item.json'
with open(file, 'w', encoding='utf-8') as f:
    try:
        print(file)
    print('[]')
