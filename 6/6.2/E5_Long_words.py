import pandas as pd

def get_long(series: pd.Series, min_length=5) -> pd.Series:

    for length, index in zip(series.values, series.index):
        if length < min_length:
            series = series.drop(index)

    return series
