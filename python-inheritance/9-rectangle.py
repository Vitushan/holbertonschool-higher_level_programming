#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


BaseGeometry = __import__('7-Base_Geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    this is a rectangle class inheritance BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")
