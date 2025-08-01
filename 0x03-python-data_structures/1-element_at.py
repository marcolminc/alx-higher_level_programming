#!/usr/bin/python3
def element_at(my_list, idx):
    if not my_list:
        return None
    my_len = len(my_list)
    if idx > my_len:
        return None
    return my_list[idx]
