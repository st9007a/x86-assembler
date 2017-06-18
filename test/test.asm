.DATA
ALPHA   DB 1
BETA    DW "a"
.CODE
        MOV AX, BX
        ADD AX, [BX]
LABEL1  MOV DX, [SI]
        ADD DX, LABEL1
