#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        val = ord(str[i])
        if 97 <= val <= 122:
            val -= 32
        print('{}'.format(chr(val)), end='')
    print()
