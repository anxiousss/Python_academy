"""Список покупок 2.0

Давайте вновь поможем человеку с покупками. Разработайте программу, которая собирает пожелания семьи в
единый список.

Формат ввода
В первой строке задано натуральное число N — количество членов семьи. В следующих NN строках записаны
желаемые продукты (через запятую и пробел).

Формат вывода
Отсортированный по алфавиту список продуктов с нумерацией.

Примечание
Помните, что итераторы можно хранить в списке, а его можно распаковать в любую функцию.

Ввод
3
картина, корзина, картонка
мыло, манка
молоко, хлеб, сыр

Вывод:
1. картина
2. картонка
3. корзина
4. манка
5. молоко
6. мыло
7. сыр
8. хлеб"""


from itertools import chain


def solution(N: int):

    stuff = []
    for _ in range(N):

        products = input().replace(',', '').split()
        stuff.append(products)

    values = sorted(list(chain.from_iterable(stuff)))

    for index, word in enumerate(values, 1):
        print(f'{index}. {word}')


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
