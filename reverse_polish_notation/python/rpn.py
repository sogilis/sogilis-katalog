#!/usr/bin/env python3

import sys
import re

def main():
  for line in sys.stdin:
    print(eval(line))

def eval(expression):
  operator = findOperator(expression)
  if operator == "none":
    return int(expression)
  else:
    elements = expression.split(operator)
    elements = list(map(int, elements))
    if operator == '+':
      return sum(elements)
    elif operator == '-': 
      return elements[0]-elements[1]

def findOperator(line):
  if line.find("+") != -1:
    return '+'
  if line.find("-") != -1:
    return '-'
  return "none"


if __name__== "__main__":
  main()
