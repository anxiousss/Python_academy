def solution(N):
    n_bunnies = 0

    for i in range(N):
        sentence = input()

        if 'зайка' in sentence:
            n_bunnies += 1

    print(n_bunnies)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
