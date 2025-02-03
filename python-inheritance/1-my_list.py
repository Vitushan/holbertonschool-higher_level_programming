#!/usr/bin/python3
"""
This is a module with the  Mylist class
"""


class MyList(list):
    def print_sorted(self):
        """
        prints the list in ascending sorted order.
        """
        print(sorted(self))
