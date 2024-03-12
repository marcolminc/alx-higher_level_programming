#!/usr/bin/python3
def uppercase(str):
    if not str:
        print('\n')
    else:
        for i in range(0, len(str)):
            print(chr(ord(str[i]) - 32) if 'a' <= str[i] <= 'z' else str[i],
                  end='' if i < len(str) - 1 else '\n')
