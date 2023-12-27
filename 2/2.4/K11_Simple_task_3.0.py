def Is_simple(N):
    if N < 2:
        return False

    for i in range(2, int(N**0.5 + 1)):
        if N % i == 0:
            return False
    else:
        return True


def solution(N):

    data = []
    n_simples = 0
    for i in range(N):

        another_n = int(input())
        data.append(another_n)

    for i in range(N):
        if Is_simple(data[i]):
            n_simples += 1

    print(n_simples)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
