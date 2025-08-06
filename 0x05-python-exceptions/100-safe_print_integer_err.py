#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format()
    Arguments:
        value: Value to attempt to print as integer
    Returns:
        bool: True if printed successfully, False otherwise
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    return True
