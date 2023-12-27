def news_line(L, N):
    for i in range(N):
        line = input()

        if len(line) <= L:
            print(line)

        else:

            print(f'{line[:L - 3:]}...')


def main():
    L = int(input())
    N = int(input())
    news_line(L, N)


if __name__ == '__main__':
    main()
