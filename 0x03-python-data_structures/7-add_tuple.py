#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = [0, 0]
    list_b = [0, 0]
    for index, i in enumerate(tuple_a):  # convert the tuple to a list
        if index < 2:
            list_a[index] = tuple_a[index]
    for index, i in enumerate(tuple_b):
        if index < 2:
            list_b[index] = tuple_b[index]
    return (list_a[0] + list_b[0], list_a[1] + list_b[1])
