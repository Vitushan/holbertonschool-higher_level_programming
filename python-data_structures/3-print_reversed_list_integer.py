#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
   reverse_num = my_list[::-1]
   for num in reverse_num:
      print("{:d}".format(num))
