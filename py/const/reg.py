reg = {
    'AX': { 'bit': 16, 'value': 0 },
    'CX': { 'bit': 16, 'value': 1 },
    'DX': { 'bit': 16, 'value': 2 },
    'BX': { 'bit': 16, 'value': 3 },
    'SP': { 'bit': 16, 'value': 4 },
    'BP': { 'bit': 16, 'value': 5 },
    'SI': { 'bit': 16, 'value': 6 },
    'DI': { 'bit': 16, 'value': 7 },
    'AL': { 'bit': 8, 'value': 0 },
    'CL': { 'bit': 8, 'value': 1 },
    'DL': { 'bit': 8, 'value': 2 },
    'BL': { 'bit': 8, 'value': 3 },
    'AH': { 'bit': 8, 'value': 4 },
    'CH': { 'bit': 8, 'value': 5 },
    'DH': { 'bit': 8, 'value': 6 },
    'BH': { 'bit': 8, 'value': 7 },
}

sreg = {
    'ES': { 'bit': 16, 'value': 0 },
    'CS': { 'bit': 16, 'value': 1 },
    'SS': { 'bit': 16, 'value': 2 },
    'DS': { 'bit': 16, 'value': 3 },
    'FS': { 'bit': 16, 'value': 4 },
    'GS': { 'bit': 16, 'value': 5 },
}

r_m_table = {
    '1': [
        { 'bit': 0, 'reg': 'BX+SI' },
        { 'bit': 1, 'reg': 'BX+DI' },
        { 'bit': 2, 'reg': 'BP+SI' },
        { 'bit': 3, 'reg': 'BP+DI' },
        { 'bit': 4, 'reg': 'SI' },
        { 'bit': 5, 'reg': 'DI' },
        { 'bit': 7, 'reg': 'BX' },
    ],

    '2': [
        { 'bit': 0, 'reg': 'BX+SI' },
        { 'bit': 1, 'reg': 'BX+DI' },
        { 'bit': 2, 'reg': 'BP+SI' },
        { 'bit': 3, 'reg': 'BP+DI' },
        { 'bit': 4, 'reg': 'SI' },
        { 'bit': 5, 'reg': 'DI' },
        { 'bit': 6, 'reg': 'BP' },
        { 'bit': 7, 'reg': 'BX' },
    ]

}
