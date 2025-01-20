#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    print_reversed_list_integer est une fonction
    qui prend en parametre:my_list
    ceci est une fonction qui imprimes les entier a l'envers.
    """
    reverse_num = my_list[::-1]
    for num in reverse_num:
        print("{:d}".format(num))
