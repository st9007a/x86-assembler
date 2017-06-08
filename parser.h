#ifndef PARSER
#define PARSER
#include "optable.h"

struct _code_data {
	unsigned int loc;
	unsigned int op;
	char *opcode;
	char *oprand_1;
	char *oprand_2;
	OpData *op_info;
};

void parse_asm(char*);
#endif
