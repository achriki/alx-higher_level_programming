#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    calc_a = tuple_a[0] if len(tuple_a) > 0 else 0
    calc_a += tuple_b[0] if len(tuple_b) > 0 else 0
    calc_b = tuple_a[1] if len(tuple_a) > 1 else 0
    calc_b += tuple_b[1] if len(tuple_b) > 1 else 0
    return calc_a, calc_b,
