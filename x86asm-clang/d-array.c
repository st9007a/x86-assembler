#include <stdio.h>
#include <stdlib.h>
#include "d-array.h"

Array new_array(int init_size) {
	Array array;
	array.elements = malloc(sizeof(void) * init_size);
	array.size = 0;
	array.max_size = init_size;
	return array;
}

void push(Array* array, void* el) {
	if (array->size == array->max_size) {
		array->elements = realloc(array->elements, array->max_size * 2);
		array->max_size *= 2;
	}
	array->elements[++array->size] = el;
}
