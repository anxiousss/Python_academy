import pandas as pd
import numpy as np


def cheque(price_list: pd.Series, **kwargs) -> pd.DataFrame:
    indexes = [i for i in range(len(price_list.index)) if price_list.index[i] in kwargs]
    ss = [(price_list.index[i], kwargs[price_list.index[i]], price_list.iloc[i]) for i in indexes]
    ss.sort(key=lambda x: x[0])
    dataframe = {'product': [], 'price': [], 'number': [], 'cost': []}

    for t in ss:
        dataframe['product'].append(t[0])
        dataframe['price'].append(t[2])
        dataframe['number'].append(t[1])
        dataframe['cost'].append(t[1] * t[2])

    return pd.DataFrame(dataframe)
