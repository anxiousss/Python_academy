def solution(a, b):
    div = a % b

    while div != 0:
        a = div
        div = b % div
        b = a

    return b


def main():
    N = int(input())
    answer = int(input())

    for i in range(N - 1):
        another_n = int(input())
        answer = solution(answer, another_n)

    print(answer)


if __name__ == '__main__':
    main()
