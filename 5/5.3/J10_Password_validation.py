from hashlib import sha256
from string import ascii_letters, digits


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8,
                        possible_chars=ascii_letters + digits, at_least_one=lambda s: s.isdigit()):
    
    if not isinstance(password, str):
        raise TypeError

    if len(password) < min_length:
        raise MinLengthError

    for s in password:
        if possible_chars.find(s) == -1:
            raise PossibleCharError

    if not any(at_least_one(s) for s in password):
        raise NeedCharError

    return sha256(password.encode('utf-8')).hexdigest()
