#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "optable.h"

typedef OpData* OpTable;

static void parse_optable(struct _op_data* opd, char* line) {
	char* split = "|";
	char* token;
	int i = 0;

	token = strtok(line, split);
	while (token != NULL) {
		char* copy = malloc(strlen(token));
		strcpy(copy, token);
		switch (i) {
			case 0:
				opd->op = strtol(copy, NULL, 16);
				break;
			case 1:
				opd->opcode = copy;
				break;
			case 2:
				opd->oprand_1 = copy;
				break;
			case 3:
				opd->oprand_2 = copy;
				break;
			case 4:
				break;
			default:
				printf("Error: unknow token: %s\n", copy);
				break;
		}
		i++;
		token = strtok(NULL, split);
	}
}

OpTable new_optable() {
	OpTable opt = malloc(sizeof(struct _op_data) * 256);
	FILE* f;
	char* line;
	size_t len = 0;
	ssize_t read = 0;
	int i = 0;

	f = fopen("./optable.txt", "r");
	if (f == NULL) {
		exit(1);
	}

	printf("---init op table---\n");
	while ((read = getline(&line, &len, f)) != -1) {
		parse_optable(&opt[i++], line);
		printf("op: %d, opcode: %s, oprand 1: %s, oprand 2: %s\n", opt[i - 1].op, opt[i - 1].opcode, opt[i - 1].oprand_1, opt[i - 1].oprand_2);
	}
	fclose(f);

	return opt;
}

