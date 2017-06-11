#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.h"

/* static Codes* new_codes() { */
/* 	Codes* codes = malloc(sizeof(Codes)); */
/* 	codes->push = push; */
/* 	return codes; */
/* }; */
/*  */
/* static void push(Codes, Code) { */
/*  */
/* }; */

static void parse_line(char* line) {
}

void parse_asm(char *asm_file) {
	FILE* f;
	char* line;
	size_t len = 0;
	ssize_t read = 0;

	f = fopen(asm_file, "r");
	if (f == NULL) {
		exit(1);
	}

	printf("---read asm file---\n");
	while((read = getline(&line, &len, f)) != 1) {
		parse_line(line);
	}

}
