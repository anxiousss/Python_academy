def make_equation(*coef):
    result = ''
    print(coef)
    coef = list(coef)
    if len(coef) == 1:
        return coef[0]

    current_variable = coef.pop()
    result = f'({make_equation(*coef)}) * x + {current_variable}'
    return result
