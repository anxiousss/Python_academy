from string import ascii_letters, digits


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError

    rus_alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper()
    for s in name:
        if s not in rus_alp:
            raise CyrillicError

    if not name[0].isupper() or not name[1:].islower():
        raise CapitalError

    return name


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


def user_validation(**kwargs):
    if [i for i in kwargs] != ['last_name', 'first_name', 'username'] or len(kwargs) != 3:
        raise KeyError

    if not all(isinstance(i, str) for i in kwargs.values()):
        raise TypeError

    name_validation(kwargs.get('last_name'))
    name_validation(kwargs.get('first_name'))
    username_validation(kwargs.get('username'))

    return kwargs
