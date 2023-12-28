import numpy as np


def stairs(vector):
    n = len(vector)
    matrix = np.zeros((n, n), dtype='int32')
    for i in range(n):
        matrix[i] = np.roll(vector, i)
    return matrix