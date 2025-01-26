#!/usr/bin/python3
def max_integer(list=[]):
    """
    Function that finds and returns the maximum integer in a list of integers.
    If the list is empty, the function returns None.
    """
    if len(list) == 0:
        return None

    result = list[0]
    i = 1

    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
