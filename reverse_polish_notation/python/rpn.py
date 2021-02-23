#!/usr/bin/env python3

import sys

operators = {
   "+": lambda stack: stack.pop() + stack.pop(),
   "-": lambda stack: -stack.pop() + stack.pop(),
   "/": lambda stack: 1 / (stack.pop() / stack.pop())
}

def main():
  stack = []

  for line in sys.stdin:
    elements = line.rstrip('\n').split(" ")
    
  for element in elements: 
    if element in operators:
      result = operators[element](stack)
    else:
      result = element
    stack.append(int(result))
  
  print(stack.pop())

if __name__== "__main__":
  main()
