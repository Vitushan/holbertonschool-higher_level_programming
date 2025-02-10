#!/usr/bin/python3
"""
Class student defining a Student
"""


class Student:
    """
    Class student defining a Student
    """

    def __init__(self, first_name, last_name, age):
        """
        initializing student instance with name , last name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return a dictionary representing a student class
        """
        return self.__dict__
