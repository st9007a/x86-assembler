#ifndef DARRAY
#define DARRAY
typedef struct _dynamic_array {
	void** elements;
	unsigned int size;
	unsigned int max_size;
} Array;

Array new_array(int);
void push(Array*, void*);
#endif
