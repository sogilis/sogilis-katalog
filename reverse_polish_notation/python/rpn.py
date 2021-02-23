#!/usr/bin/env python3

import sys

def main():
  for line in sys.stdin:
    elements = line.split(" ")
    if len(elements)==1 :
      print(elements[0])
    else:
      print(int(elements[0]) + int(elements[1]))

if __name__== "__main__":
  main()
