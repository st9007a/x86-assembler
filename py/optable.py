class OpTable:

    def __init__(self):
        self.table = {}
        with open('./optable.txt') as f:
            lines = f.readlines()
            for line in lines:
                split = line.split('|')
                self.table[split[0]] = { 'opcode': split[1], 'oprand_1': split[2], 'oprand_2': split[3] }

    def search(self, opcode):
        for op in self.table:
            if op.opcode == opcode:
                return self.table[op]

        return None

if __name__ == '__main__':
    opt = OpTable()


