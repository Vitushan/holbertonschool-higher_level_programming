#!/usr/bin/python3
"""
This is a module a square class
"""


class BaseGeometry:
    """
    this a class based in previous task
    """
    def area(self):
        """
        Return a Geometry area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        check if the args is valided integer
        """
        if value is not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        