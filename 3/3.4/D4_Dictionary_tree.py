"""Словарная ёлка

Напишите программу, которая преобразует строку слов в ёлку как показано в примере.

Формат ввода
В одну строку через пробел вводятся слова разделенные пробелом.

Формат вывода
Несколько строк. В каждой следующей строке на одно слово больше.

Примечание
accumulate «складывает» не только числа.

Ввод:
мама мыла раму

Вывод:
мама
мама мыла
мама мыла раму"""


from itertools import accumulate


def solution(sentence: str):

    sentence = sentence.split()
    sentence = [string + ' ' for string in sentence]
    for string in accumulate(sentence):
        print(string)


def main():
    sentence = input()
    solution(sentence)


if __name__ == '__main__':
    main()
