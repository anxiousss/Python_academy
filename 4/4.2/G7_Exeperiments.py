
result = []


def enter_results(*res):
    result.extend(res)


def get_sum():
    return sum(result[::2]), sum(result) - sum(result[::2])


def get_average():
    return sum(result[::2]) / len(result[::2]), (sum(result) - sum(result[::2])) / (len(result) - len(result[::2]))

