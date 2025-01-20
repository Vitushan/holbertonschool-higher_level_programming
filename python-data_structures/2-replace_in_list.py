#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    fonction replace_in_list remplace la liste
    en parametre idx et element.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
