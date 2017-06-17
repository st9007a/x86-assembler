import re
from csparser import CSParser
from oplib import Oplib

global oplib
oplib = Oplib()


class Assembler:

    def __init__(self):
        self.codes = None
        self.blocks = {'.HEAD': []}
        self.locctr = 0
        self.symtab = {}

    def load(self, file_name):
        with open(file_name) as f:
            lines =[elem.split(';')[0].strip(' ').strip('\n').strip('\r') for elem in f.readlines()]
            pos = '.HEAD'
            for line in lines:
                if len(line) == 0:
                    continue
                if line[0] == '.':
                    line = line.strip(' ')
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

            # check type ? r , m , i
            if code.oprand_1['value'] != None:
                if code.oprand_1['value'][:1] = '[':
                    code.oprand_1['type'] = 'm' # memory
                    code.oprand_1['size'] = 16
                elif oplib.is_reg(code.oprand_1) == True:
                    code.oprand_1['type'] = 'r' # register
                    code.oprand_1['size'] = oplib.get_reg_size(code.oprand_1['value'])
                elif re.match("^[0-9]+$", code.oprand_1['value']) is not None:
                    code.oprand_1['type'] = 'i'
                    if re.match("^[0-9]+$", code.oprand_1['value']) is not None:
                        code.oprand_1['size'] = 16
                    elif re.match("^[0-9a-fA-F]{2}$"):
                        code.oprand_1['szie'] = 8
                    elif re.match("^[0-9a-fA-F]{4}$"):
                        code.oprand_1['szie'] = 16
                    else:
                        raise Exception("Unknown oprand \"" + code.oprand_1['value'] + "\"")
                elif code.oprand_1['value'] in self.symtab:
                    code.oprand_1['type'] = 'm'
                    code.oprand_1['size'] = 16

            if code.oprand_2['value'] != None:
                if code.oprand_2['value'][:1] = '[':
                    code.oprand_2['type'] = 'm' # memory
                elif oplib.is_reg(code.oprand_2) == True:
                    code.oprand_2['type'] = 'r' # register
                elif re.match("^[0-9]+$", code.oprand_2['value']) is not None:
                    code.oprand_2['type'] = 'i'

            if code.oprand_1['value'] != None and code.oprand_2['value'] != None:
                for opcode in oplib.optable[code.op]:


if __name__ == '__main__':
    asm = Assembler()
    asm.load('../test/test.asm')

