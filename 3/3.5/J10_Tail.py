def tail(filename, N):

    with open(filename, 'r', encoding='UTF-8') as fin:

        text = fin.readlines()

    for line in text[-N:]:
        print(line, end='')


def main():
    filename = input()
    N = int(input())
    tail(filename, N)


if __name__ == '__main__':
    main()

