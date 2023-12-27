def solution(N, M):

    st_N = set()
    st_M = set()
    for i in range(N):
        surname = input()
        st_N.add(surname)

    for i in range(M):
        surname = input()
        st_M.add(surname)

    if len(st_N & st_M) == 0:
        print('Таких нет')
    else:
        print(len((st_N & st_M)))


def main():
    N = int(input())
    M = int(input())
    solution(N, M)


if __name__ == '__main__':
    main()
