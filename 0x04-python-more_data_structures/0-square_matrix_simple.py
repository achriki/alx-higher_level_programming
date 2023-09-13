#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for arr in matrix:
        lst = []
        for i in arr:
            lst.append(i**2)
        new_matrix.append(lst)
    return new_matrix
