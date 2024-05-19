import numpy as np


def snake(M, N, direction="H"):
    if direction == "H":
        matrix = np.arange(1, N * M + 1, dtype="int16").reshape(N, M)

        for count, line in enumerate(matrix):
            if count % 2 == 1:
                matrix[count] = line[::-1]

        return matrix

    else:
        matrix = np.arange(1, N * M + 1, dtype="int16").reshape(M, N)

        for count, line in enumerate(matrix):
            if count % 2 == 1:
                matrix[count] = line[::-1]

        return matrix.transpose()
