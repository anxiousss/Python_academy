def solution(N, penalty):
    print(f"Я больше никогда не буду писать {penalty}! \n" * N)


def main():
    N = int(input())
    penalty = input()
    solution(N, penalty)


if __name__ == "__main__":
    main()
