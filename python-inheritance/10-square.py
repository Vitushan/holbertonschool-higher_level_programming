#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


BaseGeometry = __import__('9-rectangle').BaseGeometry

class Square:
    """
    this is a square class
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        self.__width * self.__height
