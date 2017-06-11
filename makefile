all: ./output
	gcc -o output/run main.c

./output:
	mkdir -p output


run:
	./output/run

d: ./output
	gcc -o output/run main.c
	./output/run
