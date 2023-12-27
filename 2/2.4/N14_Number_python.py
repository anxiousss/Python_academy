﻿def solution(N, M):

    data = [[i * M + j + 1 for j in range(M)] for i in range(N)]
    max_ln_of_number = len(str(N * M))

    for i in range(len(data)):

        if i % 2 != 0:
            data[i].reverse()

    for line in data:

        for i in line:
            print(f'{i:{max_ln_of_number}}', end=" ")
        print()


def main():
    N = int(input())
    M = int(input())
    solution(N, M)


if __name__ == '__main__':
    main()
