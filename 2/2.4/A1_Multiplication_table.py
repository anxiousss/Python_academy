def solution(Size):

    table = []
    for i in range(1, Size + 1):
        for j in range(1, Size + 1):

            table.append(i * j)

    for i in range(0, Size**2 + 1, Size):
        print(*table[i: i + Size:])


def main():
    Size = int(input())
    solution(Size)


if __name__ == '__main__':
    main()
