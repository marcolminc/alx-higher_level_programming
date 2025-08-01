#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    my_len = len(my_list)
    if idx >= my_len:
        return my_list
    for i in range(my_len):
        if i == idx:
            my_list[i] = element
    return my_list
