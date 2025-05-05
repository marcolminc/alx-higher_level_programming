#!/usr/bin/python3
def main():
    for i in range(97, 123):
        letter = '{:c}'.format(i)
        if letter == 'e' or letter == 'q':
            continue
        print("{}".format(letter), end='')


if __name__ == "__main__":
    main()
