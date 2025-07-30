#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        sys.exit(1)

    a, op, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    if op not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    from calculator_1 import add, sub, mul, div
    operations = {'+': add, '-': sub, '*': mul, '/': div}
    result = operations[op](a, b)

    print(f"{a} {op} {b} = {result}")
