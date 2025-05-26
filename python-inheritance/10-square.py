#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this is a square class
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return (self.__width + self.__height) * 2
