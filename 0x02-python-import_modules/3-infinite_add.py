#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    args = len(sys.argv) - 1
    sum = 0
    if args > 0:
        for i in range(1, args + 1):
            sum += int(sys.argv[i])
    print('{}'.format(sum))
