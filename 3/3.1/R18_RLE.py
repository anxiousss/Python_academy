def RLE(string):
    for i in range(1, len(string)):

        a, b = string[i - 1], string[i]
        j = 0
        while a != b:
            j += 1

    print(a, j)


def main():
    string = input()
    RLE(string)


if __name__ == '__main__':
    main()
