#!/usr/bin/python3
def main():
    for i in range(122, 96, -1):
        print('{}'.format(chr(i) if i % 2 == 0 else chr(i - 32)), end='')


if __name__ == '__main__':
    main()
