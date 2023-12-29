import numpy as np


def multiplication_matrix(Size):

    matrix = np.zeros((Size, Size), dtype='int32')

    for i in range(0, Size):
        for j in range(0, Size):
            matrix[i][j] = (i + 1) * (j + 1)
    return matrix
