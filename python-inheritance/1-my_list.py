#!/usr/bin/python3
"""
Module that defines print MyList class.
"""


class MyList(list):
    """
    this is a list class sorted
    """
    def print_sorted(self):
        """
        print the list in ascending sorted order
        """
        print(sorted(self))
