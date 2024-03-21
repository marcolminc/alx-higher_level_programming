#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res_list = [replace if el == search else el for el in my_list]
    return res_list
