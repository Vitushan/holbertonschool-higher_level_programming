#!/usr/bin/python3
"""
 Class student defining a student based on task 10

"""


class Student:
    """
     Class student defining a student based on task 09

    """
    def __init__(self, first_name, last_name, age):
        """
        ...
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        ...
        """
        if isinstance(attrs, list):
            return self.__dict__
        return self.attrs
