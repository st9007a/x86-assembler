.DATA
ALPHA   DB 1
BETA    DW A1
.CODE
        MOV AX, BX
        ADD AH, 1
        ADD BL, 1A
LABEL1  ADD CL, 12A0
        MOV DL, [AL]
        ADD DL, LABEL1
