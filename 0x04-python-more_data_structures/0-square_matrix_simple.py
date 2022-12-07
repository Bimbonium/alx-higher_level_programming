#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = []  # matrix to house the squares of the passed matrix
    for rows in matrix:  # matrix is a list of lists
        temp_matrix = []  # create temporary matrix to house 2nd level
        for i in rows:  # iterate through second level
            temp_matrix.append(i ** 2)
        matrix_2.append(temp_matrix)
        # using list comprehensions
        # matrix_2 = [[i ** 2 for i in rows] for rows in matrix]
        # simple to write after writing out the complex one above
        # I should use a doc string next time
    return matrix_2
