#!/usr/bin/python3
import sys
import marshal

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: {sys.argv[0]} file.pyc")
        sys.exit(1)

    pyc_file = sys.argv[1]
    with open(pyc_file, 'rb') as f:
        header = f.read(16)
        code = marshal.load(f)
        for name in code.co_names:
            if name[0] != '_':
                print(name)
