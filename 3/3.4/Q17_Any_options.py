"""А есть ещё варианты?
Давайте вновь поможем Виталию выяснить, какие вариации вытащить из колоды определённые тройки карт возможны.
Напишите программу, которая выводит список вариантов согласно требованиям.

Формат ввода
В первой строке записана масть, которая должна присутствовать в тройке. Во второй строке записан достоинство,
которого не должно быть в тройке. В третьей строке записан предыдущий вариант полученный Виталием.

Формат вывода
Выведите следующий вариант расклада.

Примечание
Обратите внимание: валет-дама-король-туз лексикографически упорядочены. Но «10 ...» лексикографически младше,
чем «2 ...», а бубны младше, чем пики.

Масти в именительном и родительном падежах:

Именительный	Родительный
буби	        бубен
пики	        пик
трефы	        треф
черви	        червей

Ввод
пики
10
9 пик, король треф, туз червей

Вывод
9 пик, король червей, туз бубен"""


from itertools import product, permutations


def solution(exception_color: str, exception_nominal: str, last_situation: str):
    colors = ["буби", "пики", "трефы", "черви"]
    colors_change = ["бубен", "пик", "треф", "червей"]

    index = ''
    for i in range(len(colors)):

        if colors[i] == exception_color:
            index = i
            break

    compulsory_color = colors_change[index]
    nominal = sorted(["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"])
    nominal.remove(exception_nominal)

    combinations = permutations(product(nominal, colors_change), r=3)
    final_combinations = sorted(set([', '.join(' '.join(j) for j in sorted(i)) for i in combinations]))
    triads = [i for i in final_combinations if compulsory_color in i]

    for index, triad in enumerate(triads):
        if triad == last_situation:
            print(triads[index + 1])
            break


def main():
    exception_color = input()
    exception_nominal = input()
    last_situation = input()
    solution(exception_color, exception_nominal, last_situation)


if __name__ == '__main__':
    main()
