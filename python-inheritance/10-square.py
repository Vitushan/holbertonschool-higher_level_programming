#!/usr/bin/python3
"""
This is a module a square class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This is a square class
    that inherits from Rectangle
    """
    def __init__(self, size):
        """
        constructor for size
        of the square.
        The size must be positive integers.
        """
        self.__integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        return square area
        """
        return self.__width ** self.__height
