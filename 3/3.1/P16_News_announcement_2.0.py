def news_line(L, N):
    for _ in range(N):
        sentence = input()

        if L <= 3:
            break

        title = sentence
        if len(sentence) + 3 >= L:
            title = title[:L - 3] + '...'

        elif L == 4:
            title += '...'
        print(title)

        L -= len(sentence)


def main():
    L = int(input())
    N = int(input())
    news_line(L, N)


if __name__ == '__main__':
    main()
