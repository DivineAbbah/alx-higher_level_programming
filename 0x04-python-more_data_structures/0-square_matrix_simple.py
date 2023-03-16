#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for z in matrix:
        mat.append(list(map(lambda z: z**2, z)))
    return (mat)
