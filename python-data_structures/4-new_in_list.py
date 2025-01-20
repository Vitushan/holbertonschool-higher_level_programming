#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    new_in_list est une fonction qui prend en parametre
    my_list, idx et element.
    cet fonction remplace un élément dans une liste à une position
    spécifique sans modifier la liste d'origine.
    """
    my_cpylist = my_list[:]
    my_cpylist[idx] = element
    return (my_cpylist)
    if idx < 0 or idx >= len(my_list):
     return (my_list[:])
