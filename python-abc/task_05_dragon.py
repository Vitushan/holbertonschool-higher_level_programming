#!/usr/bin/python3
"""
Design two mixin classes, SwimMixin and FlyMixin
"""


class SwimMixin:
    """
    Mixin add the capacity for swim
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    add the capacity for fly
    """
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    Class dragon that can swim and fly
    """
    def roar(self):
        print("The dragon roars!")
