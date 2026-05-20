#!/usr/bin/python3
"""Integers addition.

This module defines a function for adding two integers.
It raises TypeError if a or b in neither int nor float.
"""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a(int): The integer.
        b(int): The second integer.

    Returns:
        int: sum of a and b

    Raises:
        TypeError: If a or b is not an integer

    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
