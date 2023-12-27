"""Рациональная считалочка

Напишите программу, которая производит счёт по заданным параметрам.

Формат ввода
В одну строку через пробел вводятся 3 рациональных числа — начало счета, конец и шаг.

Формат вывода
Последовательность чисел с заданными параметрами.

Ввод:
3.2 6.4 0.8

Вывод:
3.20
4.00
4.80
5.60
6.40
"""


from itertools import count


def solution(start: float, end: float, step: float):

    for value in count(start, step):

        if value <= end:
            print(f'{value:.2f}')

        else:
            break


def main():
    start, end, step = map(float, input().split())
    solution(start, end, step)


if __name__ == '__main__':
    main()
