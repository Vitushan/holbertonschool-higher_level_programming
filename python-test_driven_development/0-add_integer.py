#!/usr/bin/python3
def add_integer(a, b=98):
    """
    add two integer or float
    args: a (int, float) first number for add
    and b  is second number (int, float)
    Return: a + b (int)
    raise: TypeError: if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
