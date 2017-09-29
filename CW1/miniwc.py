#!/usr/bin/python

import sys


def read_file(file_name):
    data = ""
    if len(files) > 0:
        f = open(file_name, "r")
        data = f.read()
    return data


# TODO fix this word count
def count_words(file_name):
    return len(file_name.split(None))


def count_lines(file_name):
    lines = file_name.split("\n")
    for line in lines:
        if not line:
            lines.remove()
    return len(lines)


def character_count(file_name):
    return sum(len(word) for word in file_name)


def byte_count(file_name):
    byte = 0
    if len(file_name) > 0:
        byte = len(file_name.encode('utf-8'))+1
    return byte


if __name__ == '__main__':

    files = list(map(str, sys.argv[1:]))

    for file in files:
        temp_data = read_file(file)
        print("       " + str(count_lines(temp_data)) + "       " + str(count_words(temp_data)) + "      "
              + str(byte_count(temp_data))+" "+file)