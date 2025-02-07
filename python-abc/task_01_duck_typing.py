#!/usr/bin/python3
"""
This is a module define a shape
"""


import math
from abc import ABC, abstractmethod


def shape_info(shape):
    """
    Display perimeter and shape area
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


class Shape(ABC):
    """
    This is an abstract class Shape, inheriting ABC from the abc module.
    """

    @abstractmethod
    def area(self):
        """
        Return area shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Return perimeter shape
        """
        pass


class Circle(Shape):
    """
    that circle class a circle, which inherits from Shape
    """
    def __init__(self, radius):
        """
        this is a constructor init
        """
        self.radius = radius

    def area(self):
        """
        calculate area perimeter
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        calculate radius perimeter
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    This is an abstract class Shape, inheriting ABC from the abc module.

    """
    def __init__(self, width, height):
        """
        this is init constructor
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate a rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
        calculate perimeter
        """
        return 2 * (self.width + self.height)
