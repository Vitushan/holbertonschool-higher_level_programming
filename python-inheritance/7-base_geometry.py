#!/usr/bin/python3
"""
this is a shebang for interpreting python3
"""

class BaseGeometry:
    """
    This is a geometry Base class
    """
    def area(self):
        raise Exception("area() is not implemented")
    pass

    def integer_validator(self, name, value):
        if not isinstance(name, str):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
