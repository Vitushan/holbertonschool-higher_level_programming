#!/usr/bin/python3
"""
module shebang for interpreting python3
"""

class Square:
    """
    this is a Square class
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return f"{self.__size}"

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        return self.value

    def area(self):
        return self.__size * self.__size
