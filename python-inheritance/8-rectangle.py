#!/usr/bin/python3
"""
This is a module a square class
"""


class Rectangle:
    """
    This is a Rectangle class
    """

    def __init__(self, width, height):
        """
        constructor for width and height
        """
        if self.__width < 0 and self.__height < 0:

            self.__width = width
            self.__height = height
