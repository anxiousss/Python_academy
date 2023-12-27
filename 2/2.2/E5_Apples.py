def solution(N, M):
    Petya_apples = N + 6
    Vasya_apples = M + 9

    if Petya_apples > Vasya_apples:
        print("Петя")
    else:
        print("Вася")


def main():
    N = int(input())
    M = int(input())
    solution(N, M)


if __name__ == '__main__':
    main()
