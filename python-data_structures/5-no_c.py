#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for new_string in my_string:
        if new_string != 'c' and new_string != 'C':
            return new_string
        return my_string
