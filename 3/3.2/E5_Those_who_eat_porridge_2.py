def solution(N, M):

    data = []
    n_unique = 0
    for i in range(N + M):
        surname = input()
        data.append(surname)

    for s in data:
        if data.count(s) == 1:
            n_unique += 1

    if n_unique != 0:
        print(n_unique)
    else:
        print('Таких нет')


def main():
    N = int(input())
    M = int(input())
    solution(N, M)


if __name__ == '__main__':
    main()
