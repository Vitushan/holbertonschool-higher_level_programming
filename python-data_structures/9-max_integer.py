#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    bigger_value = my_list[0]
    for i in my_list:
        if i > bigger_value:
            bigger_value = i
    return bigger_value
