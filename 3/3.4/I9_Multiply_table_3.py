"""Таблица умножения 3.0

Местная фабрика канцелярских товаров заказала программу, которая генерирует таблицы умножения.
Давайте поможем производителю.

Формат ввода
Вводится одно натуральное число — требуемый размер таблицы.

Формат вывода
Таблица умножения заданного размера.

Примечание
itertools.product отличный способ, чтобы избавиться от вложенных циклов.

Ввод
3
Вывод
1 2 3
2 4 6
3 6 9"""


from itertools import product


def mul(data: list) -> int:

    total = 1
    for d in data:
        total *= d

    return total


def table(N: int):

    numbers = [i for i in range(1, N + 1)]

    values = list(product(numbers, numbers))

    i = 1

    for value in values:
        res = mul(value)

        if i % N != 0:
            print(res, end=' ')
        else:
            print(res)

        i += 1


def main():
    N = int(input())
    table(N)


if __name__ == '__main__':
    main()
