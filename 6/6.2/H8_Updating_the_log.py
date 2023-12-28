import pandas as pd


def update(journal: pd.DataFrame) -> pd.DataFrame:
    journal = journal.copy(deep=True)
    journal['average'] = (journal['maths'] + journal['physics'] + journal['computer science']) / 3
    journal.sort_values(by=['average', 'name'], ascending=[False, True], inplace=True)
    return journal

