#!/usr/bin/env python3

import sys
import re
def main():
  for line in sys.stdin:
    operator = findOperator(line)
    elements = re.split('\+|-',line)
    element0 = int(elements[0])
    if operator == "none":
      print(element0)
    else:
      element1 = int(elements[1])
      if operator == '+':
        print(element0+element1)
      elif operator == '-': 
        print(element0-element1)

def findOperator(line):
  if line.find("+") != -1:
    return '+'
  if line.find("-") != -1:
    return '-'
  return "none"


if __name__== "__main__":
  main()
