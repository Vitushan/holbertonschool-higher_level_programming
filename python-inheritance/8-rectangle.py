#!/usr/bin/python3
"""
this is a module for interpreting python3
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is  a rectangle class
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator('width', self.__width)
        self.integer_validator('height', self.__height)
