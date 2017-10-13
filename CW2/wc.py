#!/usr/bin/python

import sys


def main(arg):
    arguments = list(map(str, arg))
    temp_flag = ""
    temp_arg = list()
    for argument in arguments:
        file_found = True
        if argument == "-":
            print("wc: -: open: No such file or directory")
            sys.exit(0)
        elif argument == "--version" or argument == "--help":
            print("wc: illegal option -- -\n usage: wc [-clmw] [file ...]")
            sys.exit(0)
        else:
            if argument == "-l" or argument == "l" or argument == "-w" or argument == "w" or argument == "-c" \
                    or argument == "c":
                temp_flag += argument.replace("-", "")
                temp_flag.replace(" ", "")
                temp_arg.append(argument)
                file_found = False
            elif len(argument) == 3 or len(argument) == 4:
                temp_flag += argument.replace("-", "")
                temp_flag.replace(" ", "")
                temp_arg.append(argument)
                file_found = False
            if file_found.__eq__(True):
                break

    flag = list(temp_flag)
    for i in temp_arg:
        arguments.remove(i)
    output = list(arguments_split(flag, arguments, len(arguments)))
    for i in output:
        print(i)


def arguments_split(arguments, file_name, total_files_size):
    output = list()
    line_temp = ""
    word_temp = ""
    byte_temp = ""
    line = 0
    word = 0
    byte = 0
    count = 0
    total_line = 0
    total_word = 0
    total_byte = 0
    arg = arguments
    if arg.__contains__("") or len(arg) == 0:
        arg = ["l", "w", "c"]
    for file in file_name:
        if read_file(file) is not None:
            temp_data = read_file(file)
            for i in arg:
                if i == "l" or i == "-l":
                    line = count_lines(temp_data)
                    if line > -1:
                        line_temp = "\t" + str(line)
                        total_line += line
                elif i == "w" or i == "-w":
                    word = count_words(temp_data)
                    if word > -1:
                        word_temp = "\t" + str(word)
                        total_word += word
                elif i == "c" or i == "-c":
                    byte = byte_count(temp_data)
                    if byte > -1:
                        byte_temp = "\t" + str(byte)
                        total_byte += byte
                else:
                    print("wc: illegal option -- " + str(arg) + "\n" + "usage: wc [-clmw] [file ...]")
                    sys.exit(0)
        else:
            output.append("wc: " + file + " open: No such file or directory")
            break
        count += 1

        if byte_temp.__eq__(0) and word.__eq__(0):
            line_temp = "\t" + str(0)
            total_line = total_line - line
            total_line += 0

        output.append(str_builder(line_temp, word_temp, byte_temp, file))
    if total_files_size >= 2:
        temp = ""
        if line > -1:
            temp += "\t" + str(total_line)
        if word > -1:
            temp += "\t" + str(total_word)
        if byte > -1:
            temp += "\t" + str(total_byte)
        output.append(temp + " total")
    return output


def str_builder(line_temp, word_temp, byte_temp, file_name):
    return str(line_temp) + str(word_temp) + str(byte_temp) + " " + str(file_name)


def read_file(file_name):
    data = None
    try:
        f = open(file_name, "r", 1, 'utf-8')
        data = f.read()
        f.close()
    except FileNotFoundError:
        if data is None and file_name == "l" or file_name == "w" or file_name == "c":
            print("wc: " + file_name + " open: No such file or directory")
        else:
            data = None
    return data


def count_words(file_data):
    return len(file_data.split(None))


def count_lines(file_data):
    return len(file_data.split("\n")) - 1


def character_count(file_data):
    return sum(len(word) for word in file_data)


def byte_count(file_data):
    byte = 0
    if len(file_data) > 0:
        try:
            byte = len(file_data.encode('ascii'))
        except:
            byte = len(file_data.encode('utf-8'))
    return byte


if __name__ == '__main__':
    main(sys.argv[1:])
