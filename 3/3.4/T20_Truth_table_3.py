"""Таблицы истинности 3
Продолжим работу с таблицами истинности.
К сожалению, некоторые из операций Булевой алгебры не реализованы в Python.
Самые частые не стандартные операции это: импликация, строгая дизъюнкция и эквивалентность.

Обозначим их следующим образом:

импликация — ->;
строгая дизъюнкция — ^;
эквивалентность — ~.
Напишите программу, которая для введённого сложного логического высказывания строит таблицу истинности.

Формат ввода
Вводится логическое выражение от нескольких переменных.

Возможное содержание выражения:

Заглавная латинская буква — переменная;
not — отрицание;
and — конъюнкция;
or — дизъюнкция;
^ — строгая дизъюнкция;
-> — импликация;
~ — эквивалентность;
() — логические скобки.
Формат вывода
Выведите таблицу истинности данного выражения.

Примечание
Прежде, чем реализовывать новые операции, обратите внимание на их приоритет.
Рекомендуем воспользоваться знаниями полученными при решении задачи «Польский калькулятор».

Пример 1
Ввод
A -> B ~ C
Вывод
A B C F
0 0 0 0
0 0 1 1
0 1 0 0
0 1 1 1
1 0 0 1
1 0 1 0
1 1 0 0
1 1 1 1
Пример 2
Ввод
A or C ~ not (A -> B) or C
Вывод
A B C F
0 0 0 1
0 0 1 1
0 1 0 1
0 1 1 1
1 0 0 1
1 0 1 1
1 1 0 0
1 1 1 1
"""


from itertools import product


operations = {'not': 'not', 'and': 'and', 'or': 'or',
              '^': '!=', '->': '<=', '~': '=='}

priory = {'not': 0, 'and': 1, 'or': 2, '^': 3, '->': 4,
          '~': 5, '(': 6}


def rep(expression: str, variables: list) -> list:
    stack, changed_expression = [], []
    for i in expression.split():
        if i in variables:
            changed_expression.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                changed_expression.append(operations[stack.pop()])
            stack.pop()
        elif i in operations.keys():
            while len(stack) and priory[i] >= priory[stack[-1]]:
                changed_expression.append(operations[stack.pop()])
            stack.append(i)
    for i in range(len(stack)):
        changed_expression.append(operations[stack.pop()])
    return changed_expression


def result(expression: list, variables: dict) -> int:
    stack = []
    for i in range(len(expression)):
        if expression[i] in variables.keys():
            stack.append(variables[expression[i]])
        else:
            if expression[i] == 'not':
                stack.append(not stack.pop())
            else:
                a, b = stack.pop(), stack.pop()
                stack.append(eval(f'{b} {expression[i]} {a}'))
    return int(stack.pop())


def main():
    expression = input()
    final = sorted(set([i for i in expression if i.isupper()]))
    print(' '.join(final), 'F')
    variants = product([0, 1], repeat=len(final))
    expression = expression.replace('(', '( ').replace(')', ' )')
    changed_expression = rep(expression, final)
    for v in variants:
        d = {}
        for key, value in zip(final, v):
            d[key] = value
        print(' '.join(str(x) for x in v), result(changed_expression, d))


if __name__ == '__main__':
    main()
