#!/usr/bin/python3
"""
This is a module for defining a rectangle class
"""


class Rectangle:
    """
    A class to represent rectangle
    """
    number_of_instances = 0
    print_symbol = "#"


    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        number_of_instances += 1

    @property
    def width(self):
        """
         getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """
        returns the recangle area
        """
        return self.__width * self.__height

    def perimetre(self):
        """
        returns a rectangle perimeter
        """
        if width == 0 or height == 0:
            return 0
        return 2 * (self.__width + self.__height)
