#!/usr/bin/python3
"""
This is a module with the  "abc method" class
"""



from abc import ABC, abstractmethod

class Animal(ABC):
    """
    This is a Animal abstract class
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by sublasses
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
