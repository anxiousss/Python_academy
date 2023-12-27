"""Таблица истинности 2

Продолжим работу с таблицами истинности. Продумайте программу, которая для введённого сложного
логического высказывания строит таблицу истинности.

Формат ввода
Вводится логическое выражение от нескольких переменных валидное для языка Python.

Формат вывода
Выведите таблицу истинности данного выражения.

Примечание
В выражении все переменные заданы заглавными латинскими буквами.
Обратите внимание на параметры __globals и __locals у функции eval.

Ввод:
not A or B and C

Вывод:
A B C F
0 0 0 1
0 0 1 1
0 1 0 1
0 1 1 1
1 0 0 0
1 0 1 0
1 1 0 0
1 1 1 1
"""


from itertools import product


def solution(expression: str):

    variables = sorted((set(expression.replace('not', '').replace('or', '').replace('and', '').split())))
    print(*variables, 'F')

    combinations = list(product((0, 1), repeat=len(variables)))
    for combination in combinations:
        varies = dict(zip(variables, combination))

        print(*combination, int((eval(expression, varies))))


def main():
    expression = input()
    solution(expression)


if __name__ == '__main__':
    main()
