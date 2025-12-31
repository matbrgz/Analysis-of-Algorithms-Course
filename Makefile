CC = g++
CFLAGS = -Wall -Wextra -std=c++11
TARGET = sorting_app
SRC = main.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

clean:
	rm -f $(TARGET) *.o a.out
