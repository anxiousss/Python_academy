def solution(N, M, K1, K2):
    x = N * (K2 - M) // (K2 - K1)
    y = N - x
    print(x, y)


def main():
    N = int(input())
    M = int(input())
    K1 = int(input())
    K2 = int(input())
    solution(N, M, K1, K2)


if __name__ == '__main__':
    main()