#!/usr/bin/python3
"""
read and convert an JSON format by serialize technical
"""


import json
import csv


def convert_csv_to_json(csv_filename):
    """
    convert the csv file to json file
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            csv.DictReader(csv_file)
            data = [row for row in csv.DictReader(csv_file)]

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Sucess: {csv_filename} has been converted to data.json")
        return True

    except FileNotFoundError:
        print(f"Error : the file '{csv_filename}' is not found.")
        return False

    except Exception as e:
        print(f" An error occurred: {e}")
        return False
