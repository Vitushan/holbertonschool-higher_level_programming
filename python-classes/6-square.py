#!/usr/bin/python3
"""
module shebang for interpreting python3
"""


class Square:
    """
    this is a Square class with position
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")

        for num in value:
            if not isinstance(num, int) or num < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(self.__position[0] * " " + self.__size * '#')
