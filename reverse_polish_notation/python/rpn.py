#!/usr/bin/env python3

import sys
import re

def main():
  for line in sys.stdin:
    print(format(eval(line)))

def format(result):
  if result.is_integer():
    return int(result)

  return round(result, 5)

def eval(expression):
  operator = find_lowest_precedence_operator(expression)
  if operator == "none":
    return float(expression)
  else:
    elements = expression.split(operator, 1)
    if operator == '+':
      return eval(elements[0])+eval(elements[1])
    elif operator == '-': 
      return eval(elements[0])-eval(elements[1])
    elif operator == '*': 
      return eval(elements[0])*eval(elements[1])
    elif operator == '/': 
      return eval(elements[0])/eval(elements[1])

def find_lowest_precedence_operator(line):
  operators_prioritized = ["/", "*", "-", "+"]
  for op in reversed(operators_prioritized):
    if line.find(op) != -1:
      return op
  
  return "none"


if __name__== "__main__":
  main()
