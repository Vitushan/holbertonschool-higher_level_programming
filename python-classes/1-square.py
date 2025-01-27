#!/usr/bin/python3
"""
This is a module of square class based on last task.
"""


class Square:
    """
    This class defines a square with a private instance attribute: size.
    Instantiation is done with size, without type or value verification.
    """

    def __init__(self, size):
        self.__size = size
    """
    Initializes a new Square instance with the given size.
    The size is stored as a private attribute.
    """