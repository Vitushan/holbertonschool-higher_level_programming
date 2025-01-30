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
        return "\n".join([str(self.print_symbol) * self.width for _ in range(
            self.height)])

    def __repr__(self):
        """
        return a string representation of the rectangle
        to be able to recreate a new instance by using eval
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        print message "Bye rectangle..."
        when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances = - 1

    def bigger_or_equal(rect_1, rect_2):
        """
        that returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2


@classmethod
def square(cls, size=0):
    """
    returns a new Rectangle instance with width == height == size.
    """
    return
