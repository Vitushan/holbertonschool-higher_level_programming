#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this is a class inheritance from Rectangle
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
