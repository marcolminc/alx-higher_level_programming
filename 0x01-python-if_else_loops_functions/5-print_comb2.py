#!/usr/bin/python3

def main():
    for i in range(0, 100):
        print("{:02d}, ".format(i), end='')
    print(f"{99:02d}")


if __name__ == '__main__':
    main()
