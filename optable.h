#ifndef OPTABLE
#define OPTABLE
typedef struct _op_data {
	unsigned int op;
	char *opcode;
	char *oprand_1;
	char *oprand_2;
} OpData;

static void parse_optable(struct _op_data*, char*);
OpData* new_optable();
#endif
