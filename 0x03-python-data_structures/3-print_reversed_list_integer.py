#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_len = len(my_list)
        for i in range(-1, -(my_len + 1), -1):
            print('{}'.format(my_list[i]))
