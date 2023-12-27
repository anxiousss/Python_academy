def gcd(a, b):
    div = a % b

    while div != 0:
        a = div
        div = b % div
        b = a

    return b


def solution(seq):
    seq = list(map(int, seq.split('; ')))
    seq = sorted(set(seq))
    seq = list(seq)
    for i in range(len(seq)):
        mutually_simple = []
        for j in range(len(seq)):

            if i != j:

                if gcd(seq[i], seq[j]) == 1:
                    mutually_simple.append(seq[j])

        if mutually_simple:
            print(f'{seq[i]} -', end=' ')
            print(*mutually_simple, sep=', ')


def main():
    seq = input()
    solution(seq)


if __name__ == '__main__':
    main()
