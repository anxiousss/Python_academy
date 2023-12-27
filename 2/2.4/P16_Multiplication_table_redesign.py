def solution(Size, width):

    table = []
    for i in range(1, Size + 1):
        for j in range(1, Size + 1):

            table.append(i * j)

    for i in range(0, Size**2 + 1, Size):
        row = table[i: i + Size:]
        new_row = ''

        for n in row:

            new_row += str(n).center(width) + '|'

        print(new_row[:-1])

        if i < Size**2 - Size:
            print('-' * (len(new_row[:-2]) + 1))


def main():
    Size = int(input())
    width = int(input())
    solution(Size, width)


if __name__ == '__main__':
    main()
