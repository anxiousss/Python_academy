def solution(N):
    n_bunnies = 0
    for i in range(N):
        string = input()
        n_bunnies += string.count('зайка')

    print(n_bunnies)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
