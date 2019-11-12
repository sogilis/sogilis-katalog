.PHONY : test compile clean

BIN=./build/install/roman_numerals/bin/roman_numerals
TEST_RUNNER=../simple_kata_tester/simple_kata_tester.sh
TEST_CASES=../test_cases.txt

test : compile
	$(TEST_RUNNER) $(BIN) $(TEST_CASES)

compile :
	./gradlew installDist

clean :
	./gradlew clean
