#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Return: True is the object is exactly an instance of the specified class
    Return: False if otherwise.
    """
    
    return type(obj) is a_class
