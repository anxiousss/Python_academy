def solution(N, M):

    data = []
    sort_ans = []
    for i in range(N + M):
        surname = input()
        data.append(surname)

    for s in data:
        if data.count(s) == 1:
            sort_ans.append(s)

    sort_ans.sort()
    if len(sort_ans) == 0:
        print('Таких нет')
    else:
        print(*sort_ans, sep='\n')


def main():
    N = int(input())
    M = int(input())
    solution(N, M)


if __name__ == '__main__':
    main()
