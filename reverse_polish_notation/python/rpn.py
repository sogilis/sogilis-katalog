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
    elements = expression.split(operator, 1)
    if operator == '+':
      return eval(elements[0])+eval(elements[1])
    elif operator == '-': 
      return eval(elements[0])-eval(elements[1])
    elif operator == '*': 
      return eval(elements[0])*eval(elements[1])

def findOperator(line):
  if line.find("+") != -1:
    return '+'
  if line.find("-") != -1:
    return '-'
  if line.find("*") != -1:
    return '*'
  return "none"


if __name__== "__main__":
  main()
