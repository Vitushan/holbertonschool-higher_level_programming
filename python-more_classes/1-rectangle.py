#!/usr/bin/python3

"""
this is a module for defining a rectangle class
"""


class Rectangle:

    """
    A class to represent a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with optional width and height.
        Validations are performed for the parameters
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width with validation:
        - must be an integer
        - must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height with validation
        must be an integer
        must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
