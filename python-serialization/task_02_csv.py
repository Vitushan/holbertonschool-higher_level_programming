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
        with open(filename.csv, 'r') as csvfile:
            csv.DictReader(csvfile)
    except Exception:
        False
