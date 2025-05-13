#!/usr/bin/python3

def main():
    for i in range(0, 99):
        print("{:02d}, ".format(i), end='')
    print(f"{99:02d}")


if __name__ == '__main__':
    main()
