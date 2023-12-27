"""Список покупок

Поход в магазин часто вызывает проблемы. Если не подготовить список, можно уйти в магазин за хлебом, а
вернуться с десятком пакетов. Напишите программу, которая собирает пожелания семьи (мамы, папы и дочки) в единый список.

Формат ввода
В трёх строках записаны желаемые продукты (через запятую и пробел).

Формат вывода
Отсортированный по алфавиту список продуктов с нумерацией.

Примечание
Помните, что итераторы можно применять к другим итераторам.

Ввод:
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
8. хлеб
"""


def solution(string1: str, string2: str, string3: str):

    string1, string2, string3 = string1.replace(',', '').split(), \
        string2.replace(',', '').split(), string3.replace(',', '').split()
    string = string1 + string2 + string3
    string.sort()

    for index, word in enumerate(string, 1):
        print(f'{index}. {word}')


def main():
    string1 = input()
    string2 = input()
    string3 = input()
    solution(string1, string2, string3)


if __name__ == '__main__':
    main()
