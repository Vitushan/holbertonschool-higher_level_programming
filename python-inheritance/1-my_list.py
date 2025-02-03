#!/usr/bin/python3
"""
This is a module a square class
"""


class MyList(list):
    """
    this is a class Mylist
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
