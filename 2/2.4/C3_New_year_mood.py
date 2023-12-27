def solution(N):

    numbers = [i for i in range(1, N + 1)]
    j = 0

    for i in range(0, N):

        print(numbers[i:j])
        j += 1


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
