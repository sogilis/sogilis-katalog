#!/usr/bin/env python3

import sys
import re

def main():
  for line in sys.stdin:
    try:
      print(format(eval(line)))
    except ZeroDivisionError:
      print("Error_Division_By_0")

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
    if is_unary_operator(elements):
      return -float(eval(elements[1]))
    else:
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

def is_unary_operator(elements):
  return len(elements[0]) == 0

if __name__== "__main__":
  main()
