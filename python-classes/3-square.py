#!/usr/bin/python3
"""
module shebang for interpreting python3
"""


class Square:
    """
    class square
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return f"{self.__size}"
