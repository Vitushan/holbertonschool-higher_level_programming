#!/usr/bin/python3
"""
This is a module for interpreting python3
"""


class SwimMixin:
    """
    this is a mixin class
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
