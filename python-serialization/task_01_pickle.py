#!/usr/bin/python3
"""
Serialize and deserialize custom python object by the pickle module
"""


import pickle

class CustomObject:
    """
    ..
    """
    def __init__(self, name, age, is_student):
        self.name = name
        age.self = age
        is_student = is_student
    
    def display(self):
        """
        display the out object attribute
        """
        return __dict__

    def serialize(self, filename):
        """
        ...
        """
        with open(filename, "w", encoding="utf-8") as f:
            pickle.dump(filename)

        @classmethod
        def deserialize(cls, filename):
            """
            ...
            """
            with open(filename, "r", encoding="8-utf"):
                pickle.load(filename, cls)
