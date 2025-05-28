#!/usr/bin/python3
"""
This is a module for interpreting python3
"""


class Fish:
    """
    this is a Fish class
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    This is a Bird class
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    this is a multiple inheritance class
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


if __name__ == '__main__':
    flying_fish = FlyingFish()
    flying_fish.fly()
    flying_fish.swim()
    flying_fish.habitat()
