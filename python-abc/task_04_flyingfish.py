#!/usr/bin/python3
"""
this is a multiple inheritance module
"""
class Fish:
    """
    this is a fish class
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """
    this is a bird class
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    this is a multiple inheritance (fish and bird)
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish lives both in water and the sky!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
