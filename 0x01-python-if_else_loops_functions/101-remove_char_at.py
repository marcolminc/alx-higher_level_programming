#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    lst = list(str)
    lst.remove(lst[n])
    return ''.join(lst)
