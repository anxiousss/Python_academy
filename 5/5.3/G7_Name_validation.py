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

    if not name.istitle() or not name[1:].islower():
        raise CapitalError

    return name
