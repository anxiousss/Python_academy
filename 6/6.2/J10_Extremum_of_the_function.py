import pandas as pd
import numpy as np


def values(func, start, end, step):
    index = np.arange(start, end + step, step)
    return pd.Series(map(func, index), index=index, dtype='float64')


def min_extremum(data: pd.Series):
    return data.idxmin()


def max_extremum(data: pd.Series):
    return data.idxmax()
