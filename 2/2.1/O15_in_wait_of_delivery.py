def solution(N, M, T):
    minutes = N * 60 + M + T
    minutes %= 1440

    delivery_hours = minutes // 60
    delivery_minutes = minutes % 60
    print(f'{delivery_hours:02d}:{delivery_minutes:02d}')


def main():
    N = int(input())
    M = int(input())
    T = int(input())
    solution(N, M, T)


if __name__ == "__main__":
    main()
