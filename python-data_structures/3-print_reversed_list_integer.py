#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
