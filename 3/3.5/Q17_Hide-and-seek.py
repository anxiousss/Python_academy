def solution():
    with open('secrets.txt', 'r', encoding='UTF-8') as sec:

        word = sec.read()
        for s in word:
            print(''.join(chr(ord(s) & 255)), end='')


def main():
    solution()


if __name__ == '__main__':
    main()
