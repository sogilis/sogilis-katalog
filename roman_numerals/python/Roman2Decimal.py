#!/usr/bin/env python3

import sys


def main():
    params = sys.argv
    if len(params) != 2:
        return 1

    romain_numeral = params[1]
    print(romain_numeral + ":" + str(parse(romain_numeral)))


def parse(roman_numeral):
    return len(roman_numeral)


if __name__ == "__main__":
    main()
