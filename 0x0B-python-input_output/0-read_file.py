#!/usr/bin/python3
""" write a function that read from a file """


def read_file(filename=""):
    """
    Read and print content of a file.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """

    with open(filename, 'r') as f:
        content = f.read()
        print(content, end='')
