#!/usr/bin/python3
"""
this is a shebang for interpreting python3
"""


class BaseGeometry:
    """
    This is a geometry Base class
    """
    def area(self):
        """
        this is a area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate that value is a positive integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
