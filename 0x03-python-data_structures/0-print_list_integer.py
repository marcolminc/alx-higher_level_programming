#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list:
        for el in my_list:
            print('{:d}'.format(el))
