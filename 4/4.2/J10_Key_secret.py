def secret_replace(text: str, **replace_pairs) -> str:

    for started_symbol, rep in replace_pairs.items():

        rep = list(rep)

        while started_symbol in text:
            for s in rep:
                text = text.replace(started_symbol, s, 1)

    return text


result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
print(result)
