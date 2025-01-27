#!/usr/bin/python3

"""
This is a module of square class based on last task.
"""


class Square:

    """
    This class defines a square with a private instance attribute: size.
    Instantiation is done with size, with type and value checks.
    """

    def __init__(self, size=0):
        """
        Initialzes a new Square instance.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("must be >= 0")
        self.__size = size

    def area(self):
        """
        Return the current square area.
        """
        return self.__size ** 2
