def recursive_digit_sum(number):

    if number == 0:
        return number

    last_digit = number % 10
    number //= 10
    return last_digit + recursive_digit_sum(number)
