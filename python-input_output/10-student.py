#!/usr/bin/python3
"""
...
"""


class Student:
    """
    ...
    """
    def __init__(self, first_name, last_name, age):
        """
        initializing name, last name and student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        ...
        """
        attrs.__dict__
        if attrs is str:
            return self.attrs
