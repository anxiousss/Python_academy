def solution(N):
    fac = 1

    for n in range(N, 1, -1):
        fac *= n

    print(fac)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
