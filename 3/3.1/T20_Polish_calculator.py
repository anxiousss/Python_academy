def factorial(N):
    total = 1
    for x in range(2, N + 1):
        total *= x

    return total


def solution(string):

    values = string.split()
    stack = []
    for value in values:

        if value.isdigit():
            stack.append(int(value))
        else:
            if value in '+-*/':
                a = stack.pop()
                b = stack.pop()

            elif value in '~!#':
                a = stack.pop()

            elif value == '@':
                a = stack.pop()
                b = stack.pop()
                c = stack.pop()

            if value == '+':
                stack.append(a + b)

            elif value == '-':
                stack.append(b - a)

            elif value == '*':
                stack.append(a * b)

            elif value == '/':
                stack.append(b // a)

            elif value == '~':
                stack.append(-a)

            elif value == '!':
                stack.append(factorial(a))

            elif value == '#':
                stack.append(a)
                stack.append(a)

            elif value == '@':
                stack.append(b)
                stack.append(a)
                stack.append(c)

    print(*stack)


def main():
    string = input()
    solution(string)


if __name__ == '__main__':
    main()
