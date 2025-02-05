#!/usr/bin/python3
"""
This is a module defining an "abc method" class
with sublasses Dog and Cat
"""



from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing an animal.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to be implementes by suclasses.
        return a string representing the sound an animal makes
        """
        pass

class Dog(Animal):
    """
    dog  class inherits from Animal
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    cat class inherits from Animal
    """
    def sound(self):
        return "Meow"
