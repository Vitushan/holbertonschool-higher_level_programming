#!/usr/bin/python3
"""
module shebang for interpreting python3
"""
class Square:
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
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        print(f"{self.__size} * #")
        if self.__size == 0:
            print()
