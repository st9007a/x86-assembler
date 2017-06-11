#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.h"

static Code parse_line(char* line) {
	char* split = " ";
	char* token;
	int i;
	Code code;

	token = strtok(line, split);
	while (token != NULL) {
		printf("%s\n", token);
		token = strtok(NULL, split);
	}

	return code;
}

void parse_asm(char *asm_file, Array *codes) {
	FILE* f;
	char* line;
	size_t len = 0;
	ssize_t read = 0;

	f = fopen(asm_file, "r");
	if (f == NULL) {
		exit(1);
	}

	printf("---read asm file---\n");
	while((read = getline(&line, &len, f)) != -1) {
		Code code = parse_line(line);
		push(codes, &code);
	}

}
