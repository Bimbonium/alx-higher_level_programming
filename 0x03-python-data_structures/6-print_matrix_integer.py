#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for index, j in enumerate(i):
            print('{:d}'.format(j), end ='')
            if index < len(i) - 1:
                print('{}'.format(' '), end='')
        print()
