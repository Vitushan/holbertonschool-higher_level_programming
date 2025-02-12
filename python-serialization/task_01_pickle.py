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
        self.is_student = is_student

    def display(self):
        """
        display the object's attributes.
        """
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student:\
              {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            print(f"Object successfully serialized to {filename}")
        except (OSError, pickle.PickleError) as e:
            print(f"Serialization error: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file and returns an instance.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.PickleError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None
