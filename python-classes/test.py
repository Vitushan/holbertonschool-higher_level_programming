#!/usr/bin/python3


class Square:
    """
    class 
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
            raise TypeError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print ()

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(f"{self.__position[0]}" * '#' * self.__size)
