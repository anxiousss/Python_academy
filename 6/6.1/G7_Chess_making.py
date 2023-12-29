import numpy as np


def make_board(Size):

    board = np.zeros((Size, Size), dtype='int8')
    for i in range(0, Size):
        for j in range(0, Size):
            if i % 2 == j % 2:
                board[i][j] = 1

    return board
