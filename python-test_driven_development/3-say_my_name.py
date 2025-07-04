#!/usr/bin/python3
"""
this a shebang for interpreting python3
"""


def say_my_name(first_name, last_name=""):
    """
    first name and last name always strings
    otherwise raise typeError message:
    "first_name must be a string")
    print first name and last name
    returns: nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
