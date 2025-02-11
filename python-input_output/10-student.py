#!/usr/bin/python3
"""
Class student defining a student based on task 09
"""


class Student:
    """
    Class student defining a student based on task 09
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
        verify file type and  if instance list is empty or not
        """
        attrs.__dict__
        if isinstance(attrs, list):
            return self.attrs
        return self.__dict__  
