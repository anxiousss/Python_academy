def is_palindrome(something):
    if isinstance(something, int):
        return str(something) == str(something)[::-1]

    else:
        return something == something[::-1]
