#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


import json
import csv


def convert_csv_to_json(filename):
    """
    
    convert csv file to json file name data.json
    """
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            data =  list(csv.DictReader(csvfile))

        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile)
        return True
    except Exception:
        return False
