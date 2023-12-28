import pandas as pd


def best(journal: pd.DataFrame) -> pd.DataFrame:
    journal = journal.copy()
    return journal[(journal['maths'] > 3) & (journal['physics'] > 3) & (journal['computer science'] > 3)]
