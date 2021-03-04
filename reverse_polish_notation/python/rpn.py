#!/usr/bin/env python3

import sys

def main():
  for line in sys.stdin:
    elements = line.split("+")
    element0 = int(elements[0])
    if len(elements) == 1:
      print(element0)
    else:
      element1 = int(elements[1])
      print(element0+element1)


if __name__== "__main__":
  main()
