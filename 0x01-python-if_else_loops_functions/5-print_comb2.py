#!/usr/bin/python3

def main():
    for i in range(0, 100):
        print(f"{i:02d}", end='')
        print(", " if i < 99 else '\n', end='')


if __name__ == '__main__':
    main()
