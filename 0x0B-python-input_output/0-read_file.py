#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as fo:
        for line in fo:
            print(line, end='')
