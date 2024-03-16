#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    result = []
    if idx < 0 or idx >= len(my_list):
        for i in range(0, len(my_list)):
            result.append(my_list[i])
    else:
        for i in range(0, len(my_list)):
            result.append(my_list[i] if i != idx else element)
    return result
