class OpTable:

    def __init__(self):
        self.table = []
        with open('./optable.txt') as f:
            lines = f.readlines()
            for line in lines:
                split = line.split('|')
                self.table.append({ 'op': split[0], 'opcode': split[1], 'oprand_1': split[2], 'oprand_2': split[3] })

    def search(self, opcode):
        for op in self.table:
            if op['opcode'] == opcode:
                return op

        return None

if __name__ == '__main__':
    opt = OpTable()



Opt = {

    'ADD': {
        '0x00': {
            'oprand_1': 'r.m?8',
            'oprand_2': 'r?8'
        },
        '0x01': {
            'oprand_1': 'r.m?16.32',
            'oprand_2': 'r?16.32'
        },
        '0x02': {
            'oprand_1': 'r?8',
            'oprand_2': 'r.m?8',
        },
        '0x03': {
            'oprand_1': 'r?16.32',
            'oprand_2': 'r.m?16.32'
        },
        '0x04': {
            'oprand_1': 'AL',
            'oprand_2': 'i?8',
        },
        '0x05': {
            'oprand_1': 'EAX',
            'oprand_2': 'i?16.32'
        },
        '0x80': {
            'oprand_1': 'r.m?8',
            'oprand_2': 'i?8'
        },
        '0x81': {
            'oprand_1': 'r.m?16.32',
            'oprand_2': 'i?16.32'
        }
    },

    'SUB': {
        '0x28': {
            'oprand_1': 'r.m?8',
            'oprand_2': 'r?8'
        },
        '0x29': {
            'oprand_1': 'r.m?16.32',
            'oprand_2': 'r?16.32'
        },
        '0x2a': {
            'oprand_1': 'r?8',
            'oprand_2': 'r.m?8',
        },
        '0x2b': {
            'oprand_1': 'r?16.32',
            'oprand_2': 'r.m?16.32'
        },
        '0x2c': {
            'oprand_1': 'AL',
            'oprand_2': 'i?8',
        },
        '0x2d': {
            'oprand_1': 'EAX',
            'oprand_2': 'i?16.32'
        },
        '0x82': {
            'oprand_1': 'r.m?8',
            'oprand_2': 'i?8'
        },
        '0x83': {
            'oprand_1': 'r.m?16.32',
            'oprand_2': 'i?8'
        }
    },

    'CMP': {
        '0x38': {
            'oprand_1': 'r.m?8',
            'oprand_2': 'r?8'
        },
        '0x39': {
            'oprand_1': 'r.m?16.32',
            'oprand_2': 'r?16.32'
        },
        '0x3a': {
            'oprand_1': 'r?8',
            'oprand_2': 'r.m?8'
        },
        '0x3b': {
            'oprand_1': 'r?16.32',
            'oprand_2': 'r.m?16.32'
        },
        '0x3c': {
            'oprand_1': 'AL',
            'oprand_2': 'i?8'
        },
        '0x3d': {
            'oprand_1': 'EAX',
            'oprand_2': 'i?16.32'
        },
    },

    'MOV': {
        '0x88': {
            'oprand_1': 'r.m?8',
            'oprand_2': 'r?8',
        },
        '0x89': {
            'oprand_1': 'r.m?16.32',
            'oprand_2': 'r?16.32'
        },
        '0x8a': {
            'oprand_1': 'r?8',
            'oprand_2': 'r.m?8'
        },
        '0x8b': {
            'oprand_1': 'r?16.32',
            'oprand_2': 'r.m?16.32'
        }
    }
}
