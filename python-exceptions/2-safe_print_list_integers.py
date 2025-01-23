#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    try:
        while i < x:
            print(my_list[count])
            count += 1
            return count
    except Exception as e:
        pass
        print(test(e))
