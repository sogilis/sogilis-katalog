#!/usr/bin/env python3

import sys

def main():
  add = lambda a, b: a + b
  subtract = lambda a, b: a - b
  operators = {}
  operators['+']=add
  operators['-']=subtract
  stack = []
  for line in sys.stdin:
    elements = line.rstrip('\n').split(" ")
    for element in elements: 
      if element == '+' or element == '-':
        n1 = stack.pop()
        n2 = stack.pop()
        op = operators[element]
        stack.append(op(n2,n1))
      else:
        stack.append(int(element))
  print(stack.pop())

if __name__== "__main__":
  main()
