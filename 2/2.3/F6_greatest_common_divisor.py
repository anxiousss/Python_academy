def solution(n1, n2):

    while n1 != n2:
        if n1 > n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1
    print(n2)


def main():
    n1 = int(input())
    n2 = int(input())
    solution(n1, n2)


if __name__ == '__main__':
    main()
