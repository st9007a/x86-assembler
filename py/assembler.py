import re
from csparser import CSParser
from dsparser import DSParser
from oplib import Oplib

global oplib
oplib = Oplib()

class Assembler:

    def __init__(self):
        self.codes = None
        self.blocks = {'.HEAD': []}
        self.locctr = 0
        self.symtab = {}

        self.asm_file_name

    def load(self, file_name):
        self.asm_file_name = file_name
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
        if '.DATA' in self.blocks:
            self.data = [DSParser(elem) for elem in self.blocks['.DATA']]
        if '.CODE' in self.blocks:
            self.codes = [CSParser(elem) for elem in self.blocks['.CODE']]

    def write_list_file(self, code):
        with open(self.asm_file_name[:-4] + '.lst', 'a') as f:
            loc = hex(code.loc)[2:].upper() if code != None else ''
            obj_code = code.obj_code.upper() if code.obj_code != None else ''
            f.write(loc + ' ' + obj_code + ' ' + code.line + '\n')

    def pass_1(self):
        # calculate lenght of instruction
        # get address
        # store label
        global oplib

        # parse data
        if self.data != None:
            for data in self.data:


        # parse code
        for code in self.codes:
            disp = False
            if oplib.is_op_exist(code.op) == False:
                raise Exception("Unknown op \"" + code.op + "\"")

            if code.label != None:
                if code.label not in self.symtab:
                    self.symtab[code.label] = self.locctr
                else:
                    raise Exception("Duplicate label \"" + code.label + "\"")

            # check type and size ? r , m , i ? 8 , 16
            if code.oprand_1['value'] != None:
                if code.oprand_1['value'][:1] == '[':
                    code.oprand_1['type'] = 'm' # memory
                    code.oprand_1['size'] = 16
                elif oplib.is_reg(code.oprand_1['value']) == True:
                    code.oprand_1['type'] = 'r' # register
                    code.oprand_1['size'] = oplib.get_reg_size(code.oprand_1['value'])
                else:
                    disp = True
                # elif re.match("^[0-9]+$", code.oprand_1['value']) != None:
                #     code.oprand_1['type'] = 'i'
                #     code.oprand_1['size'] = 16
                # elif re.match("^[0-9a-fA-F]{2}$", code.oprand_1['value']) != None:
                #     code.oprand_1['type'] = 'i'
                #     code.oprand_1['size'] = 8
                # elif re.match("^[0-9a-fA-F]{4}$", code.oprand_1['value']) != None:
                #     code.oprand_1['type'] = 'i'
                #     code.oprand_1['size'] = 16
                # elif code.oprand_1['value'] in self.symtab:
                #     code.oprand_1['type'] = 'm'
                #     code.oprand_1['size'] = 16
                # else:
                #     raise Exception("Unknown oprand \"" + code.oprand_1['value'] + "\"")

            if code.oprand_2['value'] != None:
                if code.oprand_2['value'][:1] == '[':
                    code.oprand_2['type'] = 'm' # memory
                    code.oprand_2['size'] = 16
                elif oplib.is_reg(code.oprand_2['value']) == True:
                    code.oprand_2['type'] = 'r' # register
                    code.oprand_2['size'] = oplib.get_reg_size(code.oprand_2['value'])
                else:
                    disp = True
                # elif re.match("^[0-9]+$", code.oprand_2['value']) != None:
                #     code.oprand_2['type'] = 'i'
                #     code.oprand_2['size'] = 16
                # elif re.match("^[0-9a-fA-F]{2}$", code.oprand_2['value']) != None:
                #     code.oprand_2['type'] = 'i'
                #     code.oprand_2['size'] = 8
                # elif re.match("^[0-9a-fA-F]{4}$", code.oprand_2['value']) != None:
                #     code.oprand_2['type'] = 'i'
                #     code.oprand_2['size'] = 16
                # elif code.oprand_2['value'] in self.symtab:
                #     code.oprand_2['type'] = 'm'
                #     code.oprand_2['size'] = 16
                # else:
                #     raise Exception("Unknown oprand \"" + code.oprand_2['value'] + "\"")

            code.loc = self.locctr
            self.locctr = self.locctr + 4
            if disp == True:
                self.locctr = self.locctr + 2
            # print self.locctr
            # print code.loc
            # print code.op
            # print code.oprand_1
            # print code.oprand_2

    def pass_2(self):
        # generate opj code
        # write list file
        # write object file
        global oplib

        for code in self.codes:
            # lable
            if code.oprand_1['value'] != None and code.oprand_1['type'] == None:
                if code.oprand_1['value'] in self.symtab:
                    code.oprand_1['type'] = 'm'
                    code.oprand_1['size'] = 16
                else:
                    raise Exception("Unknown oprand_1 \"" + code.oprand_1['value'] + "\"")

            if code.oprand_2['value'] != None and code.oprand_2['type'] == None:
                if code.oprand_2['value'] in self.symtab:
                    code.oprand_2['type'] = 'm'
                    code.oprand_2['size'] = 16
                else:
                    raise Exception("Unknown oprand_2 \"" + code.oprand_2['value'] + "\"")

            opcode = oplib.get_opcode(code.op, code.oprand_1, code.oprand_2)
            mod = None
            reg = None
            rm = None
            disp = None

            # mod reg r/m
            if code.oprand_2['value'] != None and code.oprand_1['value'] != None:
                # two argument
                if code.oprand_1['type'] == 'r' and code.oprand_2['type'] == 'r':
                    mod = 3
                    reg = oplib.get_r_m_value(mod, code.oprand_1['value'])
                    rm = oplib.get_r_m_value(mod, code.oprand_2['value'])

                elif code.oprand_1['type'] == 'm' and code.oprand_2['type'] == 'r':
                    mod = 0
                    reg = oplib.get_r_m_value(mod, code.oprand_2['value'])
                    rm = oplib.get_r_m_value(mod, code.oprand_1['value'])

                    if rm == None:
                        mod = 2
                        rm = 6
                        disp = self.symtab[code.oprand_1['value']]

                elif code.oprand_1['type'] == 'r' and code.oprand_2['type'] == 'm':
                    mode = 0
                    reg = oplib.get_r_m_value(mod, code.oprand_1['value'])
                    rm = oplib.get_r_m_value(mod, code.oprand_2['value'])

                    if rm == None:
                        mod = 2
                        rm = 6
                        disp = self.symtab[code.oprand_1['value']]

            elif code.oprand_1['value'] != None:
                reg = 0
                mod = 0

                rm = oplib.get_r_m_value(mod, code.oprand_1['value'])

                if rm == None:
                    mod = 2
                    rm = 6
                    disp = self.symtab[code.oprand_1['value']]

            mod_reg_rm = mod << 6 | reg << 3 | rm
            code.obj_code = format(opcode, '02x') + format(mod_reg_rm, '02x')
            if disp != None:
                code.obj_code = code.obj_code + format(disp, '04x')



if __name__ == '__main__':
    asm = Assembler()
    asm.load('../test/test.asm')
    asm.pass_1()
    # asm.pass_2()
