.PHONY : all test clean

BIN=bin/roman_2_decimal
SRC=src/roman_2_decimal.adb
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
