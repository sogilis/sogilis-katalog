package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter romanian number: ")
	text, _ := reader.ReadString('\n')
	fmt.Println(Count(strings.TrimSpace(text)))
}

func Count(input string) int {
	return len(input)
}