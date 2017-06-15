from csparser import CSParser
from oplib import Oplib

global oplib
oplib = Oplib()


class Assembler:

    def __init__(self):
        self.codes = None
        self.blocks = {'.HEAD': []}
        self.locctr = 0

    def load(self, file_name):
        with open(file_name) as f:
            lines =[elem.split(';')[0].strip(' ').strip('\n').strip('\r') for elem in f.readlines()]
            pos = '.HEAD'
            for line in lines:
                if len(line) == 0:
                    continue
                if line[0] == '.':
                    self.blocks[line] = []
                    pos = line
                    continue
                self.blocks[pos].append(line)

        self.parse_code()

    def parse_code(self):
        self.codes = [CSParser(elem) for elem in self.blocks['.CODE']]

    def pass_1(self):
        # calculate lenght of instruction
        # get address
        # store label
        global oplib

        for code in self.codes:
            if oplib.is_op_exist(code.op) == False:
                raise Exception("Unknown op")


if __name__ == '__main__':
    asm = Assembler()
    asm.load('../test/test.asm')

