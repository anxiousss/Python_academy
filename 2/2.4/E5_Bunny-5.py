def solution(N):

    n_bunnies = 0
    for i in range(N):
        sentence = []

        while (word := str(input())) != 'ВСЁ':
            sentence.append(word)

        if 'зайка' in sentence:
            n_bunnies += 1

    print(n_bunnies)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
