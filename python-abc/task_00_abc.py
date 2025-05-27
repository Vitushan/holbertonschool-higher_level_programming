#!/usr/bin/python3
"""
This is a module for interpreting python3
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    this is a Animal class inheritance ABC
    """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return f"Bark"

class Cat(Animal):
    def sound(self):
        return f"Meow"
