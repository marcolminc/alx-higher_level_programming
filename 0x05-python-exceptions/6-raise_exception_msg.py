#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Raises a name exception.

    This function is designed specifically to demonstrate exception raising.
    Arguments:
        message: Error-describing message
    Raises:
        NameError: Always raised when this function is called
    Returns:
        None.
    """
    raise NameError(message)
