#!/usr/bin/python

import sys


def main(arg):
    files = list(map(str, sys.argv[1:]))
    for i in files:
        print(i)


if __name__ == '__main__':
    main(sys.argv[1:])
