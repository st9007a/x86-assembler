from const.optable import optable
from const.reg import *

class Oplib:

    def __init__(self):
        self.optable = optable
        self.reg = reg

    def is_op_exist(self, opc):
        return True if opc in self.optable else False

    def is_reg(self, register):
        return True if register in self.reg else False

    def get_reg_size(self, register):
        if self.is_reg(register) == False:
            raise Exception("Not a register")

        return reg[register]['bit']

    def check_direction(self, opr_1, opr_2):
        if self.is_reg(opr_1) == True and self.is_reg(opr_2) == True:
            return 1 # reg to reg
        if self.is_reg(opr_1) == True and opr_2[:1] == '[' and opr_2[-1:] == ']':
            return 1 # r/m to reg
        if opr_1[:1] == '[' and opr_1[-1:] == ']' and self.is_reg(opr_2) == True:
            return 0 # reg to r/m

    def check_size(self, opr):
        if self.is_reg(opr):
            return 1 if self.get_reg_size(opr) == 16 else 0

        # check symtable??

    def get_opcode(self, op, opr_1, opr_2):
        # filter opr_1 condition
        # filter opr_2 condition
        if self.is_op_exist(op) == False:
            raise Exception("Unknown op \"" + op + "\"")


if __name__ == '__main__':
    op = Oplib()
    print op.optable
