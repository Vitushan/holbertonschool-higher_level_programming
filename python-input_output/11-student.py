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
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            dictionary = {}
            for key in attrs:
                if hasattr(self, key):
                    dictionary[key] = getattr(self, key)
            return dictionary
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            return setattr(self, key, value)
