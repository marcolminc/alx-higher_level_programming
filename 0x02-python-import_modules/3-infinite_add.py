#!/usr/bin/python3
if __name__ == "__main__":
    total = 0
    from sys import argv

    for arg in argv[1:]:
        total += int(arg)
    print(f"{total}")
