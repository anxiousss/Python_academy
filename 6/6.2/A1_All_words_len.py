import pandas as pd


def length_stats(text: str) -> pd.Series:
    text = ''.join([s for s in text if not s.isdigit()]).lower()
    text = (text.replace(',', '').replace('.', '').
            replace('-', '').replace('/', '').replace('!', '').
            replace('?', '').replace(';', '').replace(':', ''))
    text = sorted(set(text.split()))

    lengths = [len(word) for word in text]
    information = pd.Series(lengths, text)
    return information

