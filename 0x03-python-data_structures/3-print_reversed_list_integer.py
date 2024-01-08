#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed1 = my_list[::-1]
    for i in reversed1:
        print("{:d}".format (i))
