#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Safely executes a function and handles any exceptions.

    Args:
        fct: The function to execute
        *args: Positional arguments to pass to the function

    Returns:
        The result of the function if successful, None otherwise
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
