#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    n = len(sys.argv)
    for i in range(1, n):
        sum += int(sys.argv[i])
    print("{:d}".format(sum))
