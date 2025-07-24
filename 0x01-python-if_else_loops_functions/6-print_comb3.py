#!/usr/bin/python3
def main():
    for i in range(0, 10):
        for j in range(i + 1, 10):
            print('{}{}'.format(i, j), end=', ' if i < 8 else '\n')


if __name__ == '__main__':
    main()
