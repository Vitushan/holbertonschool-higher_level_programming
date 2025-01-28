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
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square with an optional size (default is 0)
        Validates that is an integer and >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2 or not all(
            isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.size = size
        self.__position = position

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
        Setter for the size attribute
        Returns:
        value (int)
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter return position of the square(int)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.
        Returns the private attribute __position.
        """
        if not isinstance(value, tuple):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
            self.__position = position

    def area(self):
        """
        Public method to calculate the area  of the square.
        Returns: the current area of the square (size **2).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Public method to print the square.
        Prints the square using the "#" character.
        If size is 0, print an empty line.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
