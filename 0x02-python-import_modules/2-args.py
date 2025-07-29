#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = len(sys.argv) - 1
    print('{} argument'.format(args), end='')
    if args == 0:
        print('s.')
    elif args == 1:
        print(':')
    else:
        print('s:')
    if args > 0:
        for i in range(1, args + 1):
            print('{}: {}'.format(i, sys.argv[i]))
