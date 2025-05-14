#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two numbers a and b.

    a and b must be integers or floats, otherwise raise a TypeError.
    Floats are casted to integers before the addition.

    Returns the sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
