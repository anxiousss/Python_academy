def solution():
    x = 0
    y = 0

    while (direction := str(input())) != 'СТОП':
        n_steps = int(input())

        if direction == 'СЕВЕР':
            y += n_steps

        elif direction == 'ВОСТОК':
            x += n_steps

        elif direction == 'ЮГ':
            y -= n_steps

        else:
            x -= n_steps

    print(y)
    print(x)


def main():
    solution()


if __name__ == '__main__':
    main()
