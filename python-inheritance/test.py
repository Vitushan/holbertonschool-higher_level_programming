#!/usr/bin/python3

def __init__(self, size):

    self.integer_validator("size", size)
    super().__init(size)
    self.__size = size

def volume(self):
    return self.size **3