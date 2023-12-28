from math import comb


def solution(N, M):

    all_groups = comb(N, M)
    amount = comb(N - 1, M - 1)
    print(amount, all_groups)


def main():
    N, M = map(int, input().split())
    solution(N, M)


if __name__ == '__main__':
    main()
