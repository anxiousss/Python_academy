def number_rectangle(N, M):

    data = []
    numbers = [i for i in range(1, N * M + 1)]
    max_ln_of_number = len(str(N * M))

    for i in range(N):

        data.append(numbers[i::N])

    for line in data:

        for i in line:
            print(f'{i:{max_ln_of_number}}', end=" ")
        print()


def main():
    N = int(input())
    M = int(input())
    number_rectangle(N, M)


if __name__ == '__main__':
    main()
