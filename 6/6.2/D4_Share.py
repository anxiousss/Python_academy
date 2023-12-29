import pandas as pd


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


def discount(table: pd.DataFrame) -> pd.DataFrame:
    new_table = table.copy()
    new_table['cost'] = table['cost'].astype(float)
    for i in range(len(new_table.loc[:, 'cost'])):
        new_table.loc[i, 'cost'] /= 1 + (table.loc[:, 'number'][i] > 2)

    return new_table
