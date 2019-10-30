.PHONY : all test clean

RELEASE_DIR=bin/Release
BIN_NAME=roman_numerals
TEST_RUNNER=../simple_kata_tester/simple_kata_tester.sh
TEST_CASES=../test_cases.txt

all : compile post_compile

compile : clean
	dotnet build --configuration Release -o $(RELEASE_DIR)

clean :
	rm -rf $(RELEASE_DIR)

post_compile :
	rm -rf obj

test : all
	$(TEST_RUNNER) $(RELEASE_DIR)/$(BIN_NAME) $(TEST_CASES)