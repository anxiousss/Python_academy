def solution():
    total = 0

    while (number := int(input())) != 0:

        if number >= 500:
            total += number * 0.9

        else:
            total += number

    print(total)


def main():
    solution()


if __name__ == '__main__':
    main()
