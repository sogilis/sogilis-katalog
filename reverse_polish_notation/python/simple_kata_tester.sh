#!/bin/bash

#set -x

ENCODER="$1"
PATTERN_FILES="$2"

FAILING_TEST_COUNTER=0
TEST_COUNTER=0

if [ "${ENCODER:0:1}" != "/" ]
then
	ENCODER="./$ENCODER"
fi

function error()
{
	MSG=$1
	echo "$MSG" >&2
}

function usage()
{
	read -r -d '' USAGE_MSG <<  EOM
usage : $0 executable test_case_file
        Simple bash standalone tester to run simple test cases on application
        based on standard input and ouput.

	- Each line starting with a '#' is considered a comment
	- each other line is a test case described like this :
	    input_data:expected_result
EOM
	error "$USAGE_MSG"
}

function run_test()
{
	TEST_COUNTER=$(($TEST_COUNTER + 1))
	PATTERN="$1"
	EXPECTED="$2"

	OUT="$(echo "$PATTERN" | $ENCODER)"
	if [ "$OUT" == "$EXPECTED" ]
	then
		STATUS="\e[32mOK\e[39m"
		TEST_MSG=""
	else
		STATUS="\e[31mKO\e[39m"
		TEST_MSG="(obtained='$OUT', expected='$EXPECTED')"
		FAILING_TEST_COUNTER=$(($FAILING_TEST_COUNTER + 1))
	fi
	echo -e "$STATUS with input='$PATTERN' $TEST_MSG"
}

function show_results()
{
	echo "============================================================"
	echo -n "    Results : "
	if [ $FAILING_TEST_COUNTER -eq 0 ]
	then
		echo "All $TEST_COUNTER passing"
	else
		echo "$FAILING_TEST_COUNTER/$TEST_COUNTER tests failed"
	fi
}

if [ $# -ne 2 ]
then
	error "$0 is expecting two arguments"
	usage
	exit 1
fi

if [ ! -x "$ENCODER" ]
then
	error "$ENCODER is not a executable"
	usage
	exit 1
fi

while read LINE;
do
	PATTERN=$(echo $LINE |cut -d: -f1)
	EXPECTED=$(echo $LINE |cut -d: -f2)
	run_test "$PATTERN" "$EXPECTED"
done < <(cat $PATTERN_FILES | grep -Ev '^#' | grep -E '^.*:.*$')

show_results
