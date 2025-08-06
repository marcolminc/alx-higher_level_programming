#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with "{:d}".format()
    Arguments:
        value: integer to be printed
    Returns:
        True if integer is printed, False otherwise
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    return True
