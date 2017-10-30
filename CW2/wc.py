import sys
import argparse


def str_builder(line_temp, word_temp, byte_temp, file_name):
    return str(line_temp) + str(word_temp) + str(byte_temp) + " " + str(file_name)


def read_file(file_name):
    data = None
    try:
        if file_name is not "-":
            f = open(file_name, "r", 1, 'utf-8')
            data = f.read()
            f.close()
    except FileNotFoundError:
        if data is None and file_name == "-l" or file_name == "-w" or file_name == "-c":
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


class wc:
    def main(self):
        parser = self.create_parser()
        args, unknown = parser.parse_known_args()
        output = self.arguments_split(args,unknown)
        for i in output:
            print(i)

    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument('-w', action='store_true')
        parser.add_argument('-l', action='store_true')
        parser.add_argument('-c', action='store_true')
        parser.add_argument("filename", nargs='*')
        return parser

    def arguments_split(self, arguments,unknown):
        total_files_size = len(arguments.filename)
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

        if arg.c == False and arg.w == False and arg.l == False:
            arg.c = True
            arg.w = True
            arg.l = True

        if len(unknown) > 0:
            for i in unknown:
                print('wc: invalid option -- \'' + str(i) + '\'Try \'wc --help\' for more information.')
            sys.exit(0)

        for file in arguments.filename:
            if read_file(file) is not None and read_file(file) != "-":
                temp_data = read_file(file)

                if arg.l:
                    line = count_lines(temp_data)
                    line_temp = "\t" + str(line)
                    total_line += line

                if arg.w:
                    word = count_words(temp_data)
                    word_temp = "\t" + str(word)
                    total_word += word

                if arg.c:
                    byte = byte_count(temp_data)
                    byte_temp = "\t" + str(byte)
                    total_byte += byte


            else:
                output.append("wc: " + file + " open: No such file or directory")
                break
            count += 1

            if arg.c == True and arg.w == True:
                if byte_temp.__eq__(0) and word.__eq__(0):
                    line_temp = "\t" + str(0)
                    total_line = total_line - line
                    total_line += 0

            output.append(str_builder(line_temp, word_temp, byte_temp, file))
        if total_files_size >= 2:
            temp = ""
            if line > -1 and arg.l:
                temp += "\t" + str(total_line)
            if word > -1 and arg.w:
                temp += "\t" + str(total_word)
            if byte > -1 and arg.c:
                temp += "\t" + str(total_byte)
            output.append(temp + " total")
        return output


if __name__ == '__main__':
    wc().main()
