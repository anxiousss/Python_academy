def solution(string):

    values = string.split()
    stack = []
    for value in values:

        if value.isdigit():
            stack.append(int(value))
        else:
            a = stack.pop()
            b = stack.pop()

            if value == '+':
                stack.append(a + b)

            elif value == '-':
                stack.append(b - a)

            elif value == '*':
                stack.append(a * b)

    print(*stack)


def main():
    string = input()
    solution(string)


if __name__ == '__main__':
    main()
