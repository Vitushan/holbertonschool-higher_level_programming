#!/usr/bin/python3

"""
This is a module of square class based on previous task.
"""


class Square:

    """
    This class defines a square with:
    -private instance attribute: __size
    -property to get the size with getter
    -property setter to set the size
    -method to calculate the area of th square
    -method for print the square using # character
    """

    def __init__(self, size=0):
        """
        Initializes the Square with an optional size (default is 0).
        Validates that size is an integer and >= 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute.
        Returns the private attribute __size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.
        Validates that value is an integer and >= 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public method to calculate the area of the square.
        Returns: the current area of the square (size ** 2).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Public method for print the square.
        print the square using the # character.
        if size is 0, print and empty line.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
