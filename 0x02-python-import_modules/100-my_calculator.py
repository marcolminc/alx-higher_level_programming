#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        exit(1)
    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if op == '+':
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif op == '-':
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif op == '*':
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    elif op == '/':
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
