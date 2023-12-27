def total(N):
    return sum(map(int, str(N)))


def solution(N):

    data = []

    for i in range(N):
        another_n = int(input())
        data.append(total(another_n))

    print(sum(data))


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
