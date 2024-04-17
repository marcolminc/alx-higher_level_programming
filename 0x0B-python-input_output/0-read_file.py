#!/usr/bin/python3

def read_file(filename=""):
    """
    read from a file.

    :param filename: The file to be read.
    :return: Nothing.
    """

    with open(filename, 'r') as file:
        content = file.read()
        print(content, end='')
