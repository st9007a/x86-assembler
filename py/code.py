from optable import OpTable

global op_table
op_table = OpTable()

class Code:

    def __init__(self, line):
        global op_table

        self.label = None
        self.op = None
        self.oprand_1 = None
        self.oprand_2 = None
        self.loc = None
        self.obj_code = None

        self.line = line.strip('\n')
        parse_line = [elem for elem in self.line.split(' ') if elem != '']

        if op_table.search(parse_line[0]) == None:
            self.label = parse_line[0]
            self.op = parse_line[1]
        else:
            self.op = parse_line[0]

        if len(parse_line) == 3:
            self.oprand_1 = parse_line[2]
        elif len(parse_line) == 4:
            self.oprand_1 = parse_line[2].replace(',', '')
            self.oprand_2 = parse_line[3]

