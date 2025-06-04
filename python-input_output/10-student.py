#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


class Student:
    """
    this is a student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if all(isinstance(attrs, list) for atttrs in list):
            return self.__dict__
