package main

import (
	"fmt"
	"testing"
)

type testCases struct {
	input string
	want int
}

func TestCount(t *testing.T) {
	var testCases = []testCases{
		{input: "", want: 0},
		{input: "I", want: 1},
		{input: "II", want: 2},
		{input: "III", want: 3},
		{input: "IIII", want: 4},
	}
	for _, k := range testCases {
		if res := Count(k.input); res != k.want {
			fmt.Printf("Expected: %d to be equal to: %d\n", res, k.want)
			t.Fail()
		}
	}
}
