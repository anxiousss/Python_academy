from sys import stdin
from math import gcd


def solution():

    lines = [list(map(int, line.rstrip('\n').split())) for line in stdin]

    for line in lines:
        print(gcd(*line))


def main():
    solution()


if __name__ == '__main__':
    main()
