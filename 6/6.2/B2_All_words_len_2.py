import pandas as pd


def length_stats(text: str) -> tuple[pd.Series, pd.Series]:
    text = ''.join([s for s in text if not s.isdigit()]).lower()
    text = (text.replace(',', '').replace('.', '').
            replace('-', '').replace('/', '').replace('!', '').
            replace('?', '').replace(';', '').replace(':', ''))
    text = sorted(set(text.split()))

    even_stats = {word: len(word) for word in text if len(word) % 2 == 0}
    odd_stats = {word: len(word) for word in text if len(word) % 2 == 1}

    even_info = pd.Series(even_stats, dtype='int64')
    odd_info = pd.Series(odd_stats, dtype='int64')

    return odd_info, even_info


odd, even = length_stats('Мама мыла раму')
print(odd)
print(even)
