#!/usr/bin/python3

"""
this is a module for defining a rectangle class
"""


class Rectangle:
    """
    A class to represent rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with optional width and height.
        Validations are performed for the parameters
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Setter for width with validation
        must be an integer
        must be >= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """
        area returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        using the character "#".
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to recreate a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
