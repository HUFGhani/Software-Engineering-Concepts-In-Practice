#!/usr/bin/python

import sys


def read_file(file_name):
    data = None
    try:
        f = open(file_name, "r", -1, 'utf-8')
        data = f.read()
        f.close()
    except FileNotFoundError:
        print("wc: "+file_name+" open: No such file or directory")
    return data


def count_words(file_name):
    return len(file_name.split(None))


def count_lines(file_name):
    lines = file_name.split("\n")
    if len(file_name) > 0:
        for line in lines:
            if not line:
                lines.remove()
    return len(lines)


def character_count(file_name):
    return sum(len(word) for word in file_name)


def byte_count(file_name):
    byte = 0
    if len(file_name) > 0:
        byte = len(file_name.encode('ascii'))
    return byte


if __name__ == '__main__':

    files = list(map(str, sys.argv[1:]))

    for file in files:
        if len(files).__eq__(1):
            temp_data = read_file(file)
            if temp_data != "" or temp_data != "0" or temp_data is not None:
                if len(temp_data) > 0 or len(temp_data) is not None:
                    print("       " + str(count_lines(temp_data)) + "       " + str(count_words(temp_data)) + "      "
                          + str(byte_count(temp_data)) + " " + file)
                else:
                    sys.exit(0)
            else:
                sys.exit(0)
        else:
            print("Too many arguments have been passed")
            sys.exit(0)
