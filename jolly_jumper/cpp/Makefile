.PHONY : all test clean

BIN=bin/check_jolly
SRC=src/check_jolly.cpp
TEST_RUNNER=../simple_kata_tester/simple_kata_tester.sh
TEST_CASES=../test_cases.txt

all : $(BIN)

test : $(BIN)
	$(TEST_RUNNER) $< $(TEST_CASES)

clean :
	rm -f $(BIN)

$(BIN) : $(SRC)
	g++ $^ -o $@
