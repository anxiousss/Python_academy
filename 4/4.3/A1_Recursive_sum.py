def recursive_sum(*numbers):
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + recursive_sum(*numbers[1:])
