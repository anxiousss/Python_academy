def func(a, b, c):
    return ''.join(map(str, (a, b, c)))


try:
    func()
except TypeError:
    print('Ура! Ошибка!')
