import sys
import argparse


def str_builder(line_temp, word_temp, byte_temp, char_temp, lenght_temp, file_name):
    return str(line_temp) + str(word_temp) + str(byte_temp) + str(char_temp) + str(lenght_temp) + " " + str(file_name)


def read_file(file_name):
    data = None
    try:
        if file_name is not "-":
            f = open(file_name, "r", 1, 'utf-8')
            data = f.read()
            f.close()
    except FileNotFoundError:
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


def length_line(filename):
    large_line_len = 0

    with open(filename, 'r') as f:
        for line in f:
            if len(line) > large_line_len:
                large_line_len = len(line)

    return large_line_len - 1


class wc:
    def main(self):
        parser = self.create_parser()
        args, unknown = parser.parse_known_args()
        print(args)
        output = self.arguments_split(args, unknown)
        for i in output:
            print(i)

    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser()
        parser = argparse.ArgumentParser(description='Print newline, word, and byte counts for each FILE, and a total '
                                                     + 'line if\nmore than one FILE is specified.  A word is a non-zero-length '
                                                     + 'sequence of characters delimited by white space.'
                                                     + '\n\nWith no FILE, or when FILE is -, read standard input.'
                                                     + '\n\nThe options below may be used to select which counts are printed, always in'
                                                     + '\n\nthe following order: newline, word, character, byte, maximum line length.',
                                         usage='wc [OPTION]... [FILE]...\nor:  wc [OPTION]... --files0-from=F')
        parser.add_argument('-w', '--words', action='store_true', help='print the word counts')
        parser.add_argument('-l', '--lines', action='store_true', help='print the newline counts')
        parser.add_argument('-c', '--bytes', action='store_true', help='print the byte counts')
        parser.add_argument('-m', '--chars', action='store_true', help='print the character counts')
        parser.add_argument("filename", nargs='*')

        parser.add_argument('-L', '--max-line-length', action='store_true')
        parser.add_argument('--version', action='store_true')

        return parser

    def arguments_split(self, arguments, unknown):
        total_files_size = len(arguments.filename)
        output = list()
        line_temp = ""
        word_temp = ""
        byte_temp = ""
        length_temp = ""
        char_temp = ""
        line = 0
        word = 0
        byte = 0
        count = 0
        char = 0
        longLength = 0
        total_line = 0
        total_word = 0
        total_byte = 0
        total_lenght = 0
        total_char = 0
        arg = arguments

        if arg.version:
            output.append("(GNU coreutils) 8.25\nCopyright (C) 2016 Free Software Foundation, Inc.")
            output.append("License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.")
            output.append("This is free software: you are free to change and redistribute it.")
            output.append("There is NO WARRANTY, to the extent permitted by law.")
            output.append("\n")
            output.append("\n")
            output.append("Written by Paul Rubin and David MacKenzie.")
            return output

        if arg.bytes ==False and arg.words ==False and arg.lines ==False and arg.max_line_length == False and arg.chars == False:
            arg.bytes = True
            arg.words = True
            arg.lines = True

        if len(unknown) > 0:
            for i in unknown:
                output.append('wc: invalid option -- \'' + str(i) + '\'Try \'wc --help\' for more information.')
            return output

        for file in arg.filename:
            if read_file(file) is not None and read_file(file) != "-":
                temp_data = read_file(file)

                if arg.lines:
                    line = count_lines(temp_data)
                    line_temp = "\t" + str(line)
                    total_line += line

                if arg.words:
                    word = count_words(temp_data)
                    word_temp = "\t" + str(word)
                    total_word += word

                if arg.bytes and arg.chars == False:
                    byte = byte_count(temp_data)
                    byte_temp = "\t" + str(byte)
                    total_byte += byte

                if arg.chars and arg.bytes == False:
                    char = character_count(temp_data)
                    char_temp = "\t" + str(char)
                    total_char += char

                if arg.max_line_length:
                    longLength = length_line(file)
                    length_temp = "\t" + str(longLength)
                    total_lenght += longLength
            else:
                output.append("wc: " + file + " open: No such file or directory")
                break
            count += 1

            if arg.bytes == True and arg.words == True:
                if byte_temp.__eq__(0) and word.__eq__(0):
                    line_temp = "\t" + str(0)
                    total_line = total_line - line
                    total_line += 0

            output.append(str_builder(line_temp, word_temp, byte_temp, char_temp, length_temp, file))

        if total_files_size >= 2:
            temp = ""
            if line > -1 and arg.lines:
                temp += "\t" + str(total_line)
            if word > -1 and arg.words:
                temp += "\t" + str(total_word)
            if byte > -1 and arg.bytes:
                temp += "\t" + str(total_byte)
            if char > -1 and arg.chars:
                temp += "\t" + str(total_char)
            if longLength > -1 and arg.max_line_length:
                temp += "\t" + str(total_lenght)
            output.append(temp + " total")
        return output


if __name__ == '__main__':
    wc().main()