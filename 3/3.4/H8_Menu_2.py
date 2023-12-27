"""Меню питания 2.0

В детском саду ежедневно подают новую кашу на завтрак.

Напишите программу, которая строит расписание каш на ближайшие дни.

Формат ввода
Вводится натуральное число M — количество каш в меню. В каждой из последующих M строк записано одно название каши.
В конце передается натуральное число N — количество дней.

Формат вывода
Вывести список каш в порядке подачи.

Примечание
Советуем изучить документацию на функцию itertools.islice, которая реализует срезы на основе итераторов.

Ввод:
5
Манная
Гречневая
Пшённая
Овсяная
Рисовая
12

Вывод:
Манная
Гречневая
Пшённая
Овсяная
Рисовая
Манная
Гречневая
Пшённая
Овсяная
Рисовая
Манная
Гречневая"""


from itertools import islice


def solution(M: int):

    porridges = []
    for i in range(M):
        porridge = input()
        porridges.append(porridge)
    N = int(input())

    times = N // M

    if times == 0:
        print(*list(islice(porridges, N)), sep='\n')
    else:
        for i in range(times):
            print(*list(islice(porridges, M)), sep='\n')

        print(*list(islice(porridges, N - times*M)), sep='\n')


def main():
    M = int(input())
    solution(M)


if __name__ == '__main__':
    main()
