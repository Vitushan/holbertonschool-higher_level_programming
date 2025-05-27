#!/usr/bin/python3
"""
This is a module for interpreting python3
"""
from abc import ABC, abstractmethod
from math import *


class Shape(ABC):
    """
    this is a shape class with ABC inheritance
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    this is a circle class inheritance from Shape class
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * pi

    def perimeter(self):
        return 2 * self.radius * pi


class Rectangle(Shape):
    """
    this is a rectangle class
    """
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(self):
    print(f"Area: {self.area()}")
    print(f"Perimeter: {self.perimeter()}")


if __name__ == '__main__':
    shape_info(Circle)
    shape_info(Rectangle)
    c = Circle(4)
    r = Rectangle(4, 5)
    print(r)
    print(c)
