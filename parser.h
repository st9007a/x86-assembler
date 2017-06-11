#ifndef PARSER
#define PARSER
#include "optable.h"
#include "d-array.h"

typedef struct _code_data {
	unsigned int loc;
	unsigned int op;
	char *opcode;
	char *oprand_1;
	char *oprand_2;
	OpData *op_info;
} Code;

static Code parse_line(char*);
void parse_asm(char*, Array*);
#endif
