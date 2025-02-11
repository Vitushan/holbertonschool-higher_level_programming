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
        initialise first name last name and student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the instance
        """
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                key: value for key, value in self.__dict__.items()
            }

    def reload_from_json(self, json):
        """
        replace all attributes of the instance bases on the dictionary
        """
        for key, value in json.items():
            return setattr(self, key, value)
