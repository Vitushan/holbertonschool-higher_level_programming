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
    this is a class shape inherit ABC from abc
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
    that circle class  inherit  from shape
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
    Defines a rectangle class
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
