#!/usr/bin/python3
def add_integer(a, b=98):
    """
    add two integer or float
    args: int , float
    parametre: a and b
    raise: TypeError
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an")


    a = int(a)
    b = int(b)
    return a + b
