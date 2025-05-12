#!/usr/bin/python3
import copy
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        element += my_list.copy()
        return element
