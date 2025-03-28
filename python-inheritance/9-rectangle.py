#!/usr/bin/python3
"""
This is a module a square class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is a Rectangle class
    that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        constructor for width
        and height of the rectangle.
        The width and height must be positive integers.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns width x height
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns
        the string representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
