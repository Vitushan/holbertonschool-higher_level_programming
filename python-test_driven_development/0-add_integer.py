#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("amust be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an")


    a = int(a)
    b = int(b)
    return a + b
