class DSParser:

    def __init__(self, line):
        self.label = None
        self.length = None
        self.var = None
        self.loc = None

        self.line = line.strip('\n')
        parse_line = [elem for elem in self.line.split(' ') if elem != '']

        if len(parse_line) != 3:
            raise Exception('Syntax error at data section')
        elif parse_line[1] not in ['DB', 'DW']:
            raise Exception('Unknown declaration')

        self.label = parse_line[0]

        if parse_line[1] == 'DB':
            self.length = 1
        elif parse_line[1] == 'DW':
            self.length = 2

        self.var = parse_line[2] if parse_line[2][:-1] == '"' or parse_line[2][:-1] == '\'' else int(parse_line[2])


