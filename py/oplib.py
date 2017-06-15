from const.optable import optable
from const.reg import *

class Oplib:

    def __init__(self):
        self.optable = optable

    def is_op_exist(self, opc):
        return True if opc in optable else False

    def is_reg(self, register):
        return True if register in reg else False

if __name__ == '__main__':
    op = Oplib()
    print op.optable
