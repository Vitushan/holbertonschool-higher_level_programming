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
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width with validation:
        - must be an integer
        -must be >= 0
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
        """
        Setter for height with validation
        must be an integer
        must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public method to calculate the area of the rectangle
        Returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public method to calculate the rectangle perimeter
        Return the rectangle perimeter. If width or height is 0, returns 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string of the rectangle using the character "#"
        if width or height is zero return empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for _ in range(self.__height):
            rectangle.append("#" * self.__width)
        return "\n".join(rectangle)
