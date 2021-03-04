#!/usr/bin/env python3

import sys
import re
def main():
  for line in sys.stdin:
    operator = findOperator(line)
    elements = re.split('\+|-',line)
    elements = list(map(int, elements))
    if operator == "none":
      print(elements[0])
    else:
      if operator == '+':
        print(sum(elements))
      elif operator == '-': 
        print(elements[0]-elements[1])

def findOperator(line):
  if line.find("+") != -1:
    return '+'
  if line.find("-") != -1:
    return '-'
  return "none"


if __name__== "__main__":
  main()
