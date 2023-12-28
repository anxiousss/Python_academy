from math import prod, pow


def mid(seq):

    seq_prod = prod(seq)
    print(pow(seq_prod, 1 / len(seq)))


def main():

    seq = list(map(float, input().split()))
    mid(seq)


if __name__ == '__main__':
    main()
