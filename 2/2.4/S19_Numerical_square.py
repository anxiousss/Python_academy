def numerical_square(size):
    matrix = [
        [min(i + 1, j + 1, size - i, size - j) for j in range(size)]
        for i in range(size)
    ]

    for row in matrix:

        if size >= 19:
            if 10 in row:
                print(" ", end='')
                for i in range(1, len(row)):

                    a, b = row[i - 1], row[i]
                    if b < 10:
                        print(a, end='  ')

                    else:
                        print(a, end=' ')

                print(1, end='')
                print()

            else:
                print(" ", end='')
                print("  ".join(map(str, row)))

        else:
            print(*row)


def main():
    size = int(input())
    numerical_square(size)


if __name__ == "__main__":
    main()
