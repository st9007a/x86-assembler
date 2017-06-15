optable = {

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
        },
        '0x8c': {
            'oprand_1': 'r.m?16',
            'oprand_2': 'Sreg'
        },
        '0x8e': {
            'oprand_1': 'Sreg',
            'oprand_2': 'r.m?16'
        },
        '0xb0': {
            'oprand_1': 'AL',
            'oprand_2': 'i?8'
        },
        '0xb1': {
            'oprand_1': 'CL',
            'oprand_2': 'i?8'
        },
        '0xb2': {
            'oprand_1': 'DL',
            'oprand_2': 'i?8'
        },
        '0xb3': {
            'oprand_1': 'BL',
            'oprand_2': 'i?8'
        },
        '0xb4': {
            'oprand_1': 'AH',
            'oprand_2': 'i?8'
        },
        '0xb5': {
            'oprand_1': 'CH',
            'oprand_2': 'i?8'
        },
        '0xb6': {
            'oprand_1': 'DH',
            'oprand_2': 'i?8'
        },
        '0xb7': {
            'oprand_1': 'BH',
            'oprand_2': 'i?8'
        }
    },

    'CALL': {
        '0xe8': {
            'oprand_1': 'rel?16.32'
        }
    },

    'JMP': {
        '0xe9': {
            'oprand_1': 'rel?16.32'
        },
        '0xeb': {
            'oprand_1': 'rel?8'
        }
    },
    'JNL': {
        '0x7d': {
            'oprand_1': 'rel?8'
        },
        '0x0f8d': {
            'oprand_1': 'rel?16.32'
        }
    },
    'JGE': {
        '0x7d': {
            'oprand_1': 'rel?8'
        },
        '0x0f8d': {
            'oprand_1': 'rel?16.32'
        }
    },
    'JLE': {
        '0x7e': {
            'oprand_1': 'rel?8'
        },
        '0x0f8e': {
            'oprand_1': 'rel?16.32'
        }
    },

    'JNG': {
        '0x7e': {
            'oprand_1': 'rel?8'
        },
        '0x0f8e': {
            'oprand_1': 'rel?16.32'
        }
    }
}

