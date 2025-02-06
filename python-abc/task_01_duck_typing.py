#!/usr/bin/python3
"""
This is a module defining an "abc method" class
with sublasses Dog and Cat
"""


from abc import ABC, abstractmethod
import math
class Shape(ABC):
    def shape_info(Shape):
        """
        Display perimeter and shape area
        """
        print(f"area: {Shape.area()}")
        print(f"perimeter: {Shape.perimeter()}")
    """
    '((()))
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
    ;;;
    """
    def __init__(self, radius):
        """
        kgjgnjkn
        """
        self.radius = radius

    def area(self):
        """
        calculate area perimeter
        """
        return math.pi * radius ** 2

    def perimeter(self, radius):
        """
        calculate radius perimeter 
        """
        return 2 * math.pi * radius
    
class Rectangle(Shape):
    """
    Defines a rectangle class
    """
    def __init__(self, width, height):
        """
        ljgnjnglr
        """
        self.width = width
        self.height = height

    def area(self, width, height):
        """
        Calculate a rectangle area
        """
        return self.width * self.height

    def perimeter(self, width, height):
        """
        fbfgb
        """
        return 2 * (self.width + self.height)

