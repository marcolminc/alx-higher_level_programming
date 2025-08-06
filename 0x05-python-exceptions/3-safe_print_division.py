#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result.
    Arguments:
        a: Dividend
        b: Divisor
    Returns:
        float: Result of division, None if division by zero
    """
    res = None
    try:
        res = a / b
    except ZeroDivisionError:
        pass
    finally:
        print('Inside result: {}'.format(res))
    return res
