#!/usr/bin/env python3

import sys
import re
def main():
  for line in sys.stdin:
    operator = line[1]
    elements = re.split('\+|-',line)
    element0 = int(elements[0])
    if len(elements) == 1:
      print(element0)
    else:
      element1 = int(elements[1])
      if operator == '+':
        print(element0+element1)
      elif operator == '-': 
        print(element0-element1)


if __name__== "__main__":
  main()
