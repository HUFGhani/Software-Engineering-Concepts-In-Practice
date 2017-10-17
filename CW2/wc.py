import sys
import argparse


class wc:
    def main(self):
        args = self.create_parser()
        output = self.arguments_split(args, args.filename, len(args.filename))
        for i in output:
            print(i)

    def create_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-w', action='store_true')
        parser.add_argument('-l', action='store_true')
        parser.add_argument('-c', action='store_true')
        parser.add_argument("filename", nargs='*')
        args = parser.parse_args()
        return args

    def arguments_split(self, arguments, file_name, total_files_size):
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

        for file in file_name:
            if self.read_file(file) is not None:
                temp_data = self.read_file(file)

                if arg.l:
                    line = self.count_lines(temp_data)
                    line_temp = "\t" + str(line)
                    total_line += line

                if arg.w:
                    word = self.count_words(temp_data)
                    word_temp = "\t" + str(word)
                    total_word += word

                if arg.c:
                    byte = self.byte_count(temp_data)
                    byte_temp = "\t" + str(byte)
                    total_byte += byte
                elif arg.c:
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

            output.append(self.str_builder(line_temp, word_temp, byte_temp, file))
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

    @staticmethod
    def str_builder(line_temp, word_temp, byte_temp, file_name):
        return str(line_temp) + str(word_temp) + str(byte_temp) + " " + str(file_name)

    @staticmethod
    def read_file(file_name):
        data = None
        try:
            f = open(file_name, "r", 1, 'utf-8')
            data = f.read()
            f.close()
        except FileNotFoundError:
            if data is None and file_name == "-l" or file_name == "-w" or file_name == "-c":
                print("wc: " + file_name + " open: No such file or directory")
            else:
                data = None
        return data

    @staticmethod
    def count_words(file_data):
        return len(file_data.split(None))

    @staticmethod
    def count_lines(file_data):
        return len(file_data.split("\n")) - 1

    @staticmethod
    def character_count(file_data):
        return sum(len(word) for word in file_data)

    @staticmethod
    def byte_count(file_data):
        byte = 0
        if len(file_data) > 0:
            try:
                byte = len(file_data.encode('ascii'))
            except:
                byte = len(file_data.encode('utf-8'))
        return byte


if __name__ == '__main__':
    wc().main(sys.argv[1:])
