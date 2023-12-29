from string import ascii_letters, digits


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username):

    alp = ascii_letters + digits + '_'
    if not isinstance(username, str):
        raise TypeError

    for s in username:
        if s not in alp:
            raise BadCharacterError

    if username[0] in digits:
        raise StartsWithDigitError

    return username
