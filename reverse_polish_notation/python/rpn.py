#!/usr/bin/env python3

import sys

def main():
  stack = []
  for line in sys.stdin:
    elements = line.rstrip('\n').split(" ")
    for element in elements: 
      if element == '+' or element == '-':
        n1 = stack.pop()
        n2 = stack.pop()
        if element == '+':
          stack.append(n2+n1)
        else:
          stack.append(n2-n1)
      else:
        stack.append(int(element))
  print(stack.pop())

if __name__== "__main__":
  main()
