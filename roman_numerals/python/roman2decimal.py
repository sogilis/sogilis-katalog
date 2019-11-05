#!/usr/bin/env python3

import sys

def main():
    count = -1

    while True:
        c = sys.stdin.read(1)
        if not c:
            break

        count += 1

    if count:
        print(count)
  
if __name__== "__main__":
  main()
