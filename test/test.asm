.DATA
ALPHA   DB 1
BETA    DW A1
.CODE
        MOV AX, BX
        ADD AX, [BX]
LABEL1  MOV DX, [AL]
        ADD DX, LABEL1
