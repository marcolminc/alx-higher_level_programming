#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Safely prints x elements from a list.

    Args:
        my_list: List to print elements from
        x: number of elements to attempt printing

    Returns:
        Number of elements actually printed
    """
    count = 0
    for i in range(x):
        try:
            print('{}'.format(my_list[i]), end='')
            count += 1
        except IndexError:
            break
    print()
    return count
