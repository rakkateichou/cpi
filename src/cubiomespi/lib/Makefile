CC = gcc
CFLAGS = -fPIC -m64
LDFLAGS = -shared

# Detect OS to set the correct output extension
ifeq ($(OS),Windows_NT)
    OUT = lib.dll
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Darwin)
        OUT = lib.dylib
    else
        OUT = lib.so
    endif
endif

SRCS = newlib.c \
       cubiomes/util.c \
       cubiomes/noise.c \
       cubiomes/layers.c \
       cubiomes/generator.c \
       cubiomes/finders.c \
       cubiomes/biometree.c \
       cubiomes/biomenoise.c

all: $(OUT)

$(OUT): $(SRCS)
	$(CC) $(LDFLAGS) -o $(OUT) $(CFLAGS) $(SRCS)

clean:
	rm -f *.dll *.so *.dylib
