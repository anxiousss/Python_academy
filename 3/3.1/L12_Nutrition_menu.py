def menu(N):
    data = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

    i = 0
    j = 0
    while True:
        if j == N:
            break

        if i == 4:
            print(data[i])
            i = 0
            j += 1

        else:

            print(data[i])
            i += 1
            j += 1


def main():
    N = int(input())
    menu(N)


if __name__ == '__main__':
    main()
