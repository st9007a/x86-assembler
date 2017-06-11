#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.h"

static Array to_str_array(char* line, char* split) {
	Array array = new_array(1);
	char* token = strtok(line, split);
	while (token != NULL) {
		char* copy = malloc(strlen(token) + 1);
		copy[strlen(token)] = 0;
		push(&array, copy);
	}
	return array;
}

static Code parse_line(char* line) {
	int i;
	Code code;
	Array code_arr = to_str_array(line, " ");

	return code;
}

static int is_valid_format(char* line) {
	int i;
	int len = strlen(line);
	for (i = 0; i < len; i++) {
		if (line[i] != ' ') {
			break;
		}
	}

	if (i == len || i < len && line[i + 1] == ';') {
		return 0;
	}
	return 1;
}

void parse_asm(char* asm_file, Array* codes) {
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
		if (is_valid_format(line) == 0) {
			continue;
		}
		Code code = parse_line(line);
		push(codes, &code);
	}

}
