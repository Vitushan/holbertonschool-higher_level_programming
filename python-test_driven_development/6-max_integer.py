#!/usr/bin/python3
"""
Module 6-max_integer
Cette fonction retourne le maximum d'une liste.
"""

def max_integer(list=[]):
    """
    Trouve et retourne le maximum d'une liste.

    Paramètres :
    list : liste d'entiers ou flottants (facultatif).

    Retourne :
    - Le maximum de la liste.
    - None si la liste est vide.
    """
    if len(list) == 0:
        return None
    max_value = list[0]
    for num in list:
        if num > max_value:
            max_value = num
    return max_value
