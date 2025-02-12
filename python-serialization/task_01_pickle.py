#!/usr/bin/python3
"""
Serialize and deserialize custom python object by the pickle module
"""


import pickle

class CustomObject:
    """
    A custom class with serialization and deserialization methods.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        is_student = is_student
    
    def display(self):
        """
        display the object's attributes.
        """
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file.
        """
        with open(filename, "wb", encoding="utf-8") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file and returns an instance.
        """
        with open(filename, "rb", encoding="8-utf") as f:
            return pickle.load(f)
