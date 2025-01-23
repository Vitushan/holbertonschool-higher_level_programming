#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i])
            count += 1
        except TypeError:
            pass
        print()
        return count
