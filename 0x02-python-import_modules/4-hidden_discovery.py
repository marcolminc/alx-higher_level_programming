#!/usr/bin/python3

if __name__ == "__main__":
    import importlib.util
    import sys

    pyc_path = './hidden_4.pyc'
    spec = importlib.util.spec_from_file_location("hidden_4", pyc_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    names.sort()
    for name in names:
        print(name)
