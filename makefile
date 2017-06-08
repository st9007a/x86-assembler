all: ./output
	gcc -o output/run main.c

./output:
	mkdir -p output


run:
	./output/run

debug: ./output
	gcc -o output/run main.c
	./output/run
