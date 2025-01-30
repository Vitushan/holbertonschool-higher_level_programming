#!/usr/bin/python3
"""
Thisvis a module for defining a rectangle class
"""


class Rectangle:
    """
    A class to represent rectangle
    """
    number_of_instanceqs = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with optional width and height
        validations are performed for the parameters
        """
        