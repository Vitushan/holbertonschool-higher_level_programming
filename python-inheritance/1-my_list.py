#!/usr/bin/python3
"""
Module that defines print sorted.
"""


class MyList(list):
    """
    this is a list class sorted
    """
    def print_sorted(self):
        print(sorted(self))
