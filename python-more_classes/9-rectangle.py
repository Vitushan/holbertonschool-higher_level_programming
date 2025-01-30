#!/usr/bin/python3
"""
This is a module for defining a rectangle class
"""


class Rectangle:
    """
    A class to represent rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with optional width and height
        validations are performed for the parameters
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        getter for width"
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """
        returns  a rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns a rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        print the rectangle with the character "#"
        """
        if self.__width == 0 or self.__height:
            return ""
        return "\n".join([str(self.print_symbol
                              ) * self.width for _ in range (self.height)])

    def __repr__(self):
        """
        return a string representation of the rectangle
        to be able to recreate a new instance by using eval
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        
