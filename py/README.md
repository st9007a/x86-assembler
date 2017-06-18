# x86 assembler

## Note

1. Not support comment
2. Not support any prefix symbol
3. Not support immediate addresing mode
4. Use `space` instead of `tab`
5. Only support `.DATA` and `.CODE` segment
6. `CALL` and `J` only support rel
7. Register you can use see `const/reg.py`
8. Test file at `test/test.asm`

## Usage

`python assembler.py [ASM FILE] -o [LIST FILE]`

ex: `python assembler.py test.asm -o test.lst`
