HEADERS = client.h utils.h
LIBS = -lmsquic
INCLUDE = -I/opt/msquic/src/inc/ -I./
CFLAGS = -O0 -g

default: client
all: client server


server: server.c utils.c
	gcc $(CFLAGS) utils.c server.c -o server $(INCLUDE) -L./ $(LIBS)

client.o: client.c $(HEADERS)
	gcc $(CFLAGS) -c client.c -o client.o $(INCLUDE)

utils.o: utils.c $(HEADERS)
	gcc $(CFLAGS) -c utils.c -o utils.o $(INCLUDE) 

client: client.o utils.o
	gcc $(CFLAGS) utils.o client.o -o client $(INCLUDE) -L./ $(LIBS)

clean:
	-rm -f server.o client.o utils.o
	-rm -f server client utils
