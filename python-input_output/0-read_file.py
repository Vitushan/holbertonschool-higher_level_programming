#!/usr/bin/python3
"""
read a utf-8 txt file and prints it to stdout
"""


def read_file(filename=""):
    """
    for read a file encoding utf-8
    """
 
    with open(filename, "r", encoding = "utf-8") as f:
        print(f.read(), end="")
