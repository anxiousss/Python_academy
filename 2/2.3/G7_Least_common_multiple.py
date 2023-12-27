def solution(n1, n2):
    mul = n1 * n2

    while n1 != 0 and n2 != 0:

        if n1 > n2:
            n1 %= n2

        else:
            n2 %= n1

    print(mul // (n1 + n2))


def main():
    n1 = int(input())
    n2 = int(input())
    solution(n1, n2)


if __name__ == '__main__':
    main()
