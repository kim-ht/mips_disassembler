#Makefile
#by kimht

#macros
OBJECTS = base.o disassembler.o
CC = gcc
CFLAGS = -Wall -c

main: $(OBJECTS)
	$(CC) -Wall main.c $(OBJECTS) -o main

base.o: ./base/base.c ./base/base.h
	$(CC) $(CFLAGS) ./base/base.c

disassembler.o: ./disassembler/disassembler.c ./disassembler/disassembler.h
	$(CC) $(CFLAGS) ./disassembler/disassembler.c

clean:
	rm $(OBJECTS) main
