"""def make_linear(array):

    linear_array = []

    for x in linear_array:
        if isinstance(x, list):
            break

    else:
        return array

    for x in array:

        if isinstance(x, list):
            return make_linear(x)

        linear_array.append(x)

    return linear_array


linear_array = make_linear([1, 2, [3]])
print(linear_array)
"""


def make_linear(lst):
    linear_array = []
    for i in lst:
        if isinstance(i, list):
            linear_array.extend(make_linear(i))
        else:
            linear_array.append(i)
    return linear_array
