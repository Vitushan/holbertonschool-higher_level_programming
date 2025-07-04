#!/usr/bin/python3
"""
Module that defines the MyList class.
"""


class MyList(list):
    """
    MyList inherits from list and adds a method to print the list sorted.
    """
    def print_sorted(self):
        """
        print ascending sort list
        """
        print(sorted(self))
