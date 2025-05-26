#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


BaseGeometry = __import__('9-rectangle').BaseGeometry


def __init__(self, size):
    """
    this is a size init
    """
    self.__size = size
    self.integer_validator("size", self.__size)

def area(self):
    self.__width * self.__height
