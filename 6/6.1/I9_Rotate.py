import numpy as np


def rotate(array, deg):

    match deg:
        case 90:
            return np.rot90(array, -1)
        case 180:
            return np.rot90(np.rot90(array))
        case 270:
            return np.rot90(array)
        case 360:
            return array
