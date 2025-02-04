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

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        return square area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns
        the string representation of the square
        """
        return f"[Square] {self.__size}/{self.__size}"
