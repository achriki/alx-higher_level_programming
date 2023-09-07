#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = len(sys.argv)
    if n > 2:
        print("{:d} arguments:".format(n - 1))
    if n == 1:
        print("0 arguments.")
    if n == 2:
        print("1 argument:")
    for i in range(1, n):
        print("{:d}: {:s}".format(i, sys.argv[i]))
