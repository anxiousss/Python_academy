def solution():
    n_bunnies = 0

    while (sentence := str(input())) != 'Приехали!':

        if 'зайка' in sentence:
            n_bunnies += 1

    print(n_bunnies)


def main():
    solution()


if __name__ == '__main__':
    main()
