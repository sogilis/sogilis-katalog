#!/usr/bin/env python3

import sys

def main():
  stack = []
  for line in sys.stdin:
    elements = line.rstrip('\n').split(" ")
    for element in elements: 
      if element != '+':
        stack.append(int(element))
      else:
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n1+n2)
  print(stack.pop())

if __name__== "__main__":
  main()
