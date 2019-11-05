.PHONY : all test clean

BIN=bin/check_jolly
SRC=src/check_jolly.adb
TEST_RUNNER=../simple_kata_tester/simple_kata_tester.sh
TEST_CASES=../test_cases.txt

all : $(BIN)

test : $(BIN)
	$(TEST_RUNNER) $< $(TEST_CASES)

clean :
	rm -rf bin

$(BIN) : $(SRC)
	mkdir -p bin
	gnatmake $^ -D bin -o $@
