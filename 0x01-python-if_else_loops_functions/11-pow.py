#!/usr/bin/python3
def pow(a, b):
    result = a
    if b == 0:
        return 1
    elif b < 0:
        result = 1
        for i in range(0, -b):
            result /= a
    else:
        for i in range(1, b):
            result *= a
    return result


print(pow(-98, -10))
