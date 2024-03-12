#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if 97 <= ord(str[i]) <= 123:
            print('{:s}'.format(chr(ord(str[i]) - 32)),
                  end='' if i < len(str) - 1 else '\n')
        else:
            print('{:s}'.format(str[i]), end='' if i < len(str) - 1 else '\n')
