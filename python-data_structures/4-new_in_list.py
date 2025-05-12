#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        new_list = my_list.copy()
        element[idx] += new_list
        return new_list
    return my_list
