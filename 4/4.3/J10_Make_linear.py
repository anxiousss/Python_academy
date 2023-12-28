def make_linear(lst):
    linear_array = []
    for i in lst:
        if isinstance(i, list):
            linear_array.extend(make_linear(i))
        else:
            linear_array.append(i)
    return linear_array
