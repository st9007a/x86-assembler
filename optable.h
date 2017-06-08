#ifndef OPTABLE
#define OPTABLE
struct _op_data {
	unsigned int op;
	char *opcode;
	char *oprand_1;
	char *oprand_2;
};

struct _op_data* init_optable();
void parse_optable(struct _op_data*, char*);
#endif