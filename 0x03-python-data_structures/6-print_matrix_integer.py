#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for i in lst:
            print("{:d}".format(i), end=" "
                  if i != lst[-1] else '\n')
