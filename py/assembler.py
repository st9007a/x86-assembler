from optable import OpTable
from code import Code

global op_table
op_table = OpTable()

class Assembler:

    def __init__(self):
        self.codes = None
        self.blocks = {'.HEAD': []}

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
        self.codes = [Code(elem) for elem in self.blocks['.CODE']]
        print self.codes



if __name__ == '__main__':
    asm = Assembler()
    asm.load('../test/uASM-TV01A.asm')

