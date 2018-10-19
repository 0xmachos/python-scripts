#!/usr/bin/env python3
# python-scripts/template.py

# template.py
#   Template for starting new python scripts

## Imports
import sys


def usage():
    print("How to use template.py ")
    exit(1)


def main():
    args = sys.argv[1:]

    if len(args) == 0:
    	usage()

    arg = sys.argv[1]
    print(arg)

    exit(0)


if __name__== "__main__":
    main()
