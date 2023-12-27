"""def solution():
    with open('numbers.num', 'rb') as fin:
        s = list(fin.read())

        total = 0
        for i in range(1, len(s) + 1, 2):
            total += s[i - 1] * 16**2 + s[i]

    print(total % 2 ** 16)


def main():
    solution()


if __name__ == '__main__':
    main()"""


def solution():
    with open('numbers.num', 'rb') as fin:
        num = fin.read()
        # print(sum([int.from_bytes(data[i:i + 2], "big") for i in range(0, len(data), 2)]) % 2**16)
    total = 0
    for i in range(0, len(num), 2):
        total += int.from_bytes(num[i:i + 2], 'big')

    print(total % 2**16)


def main():
    solution()


if __name__ == "__main__":
    main()
