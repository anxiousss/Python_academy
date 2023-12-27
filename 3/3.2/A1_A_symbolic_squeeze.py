def solution(string):
    string = set(string)
    print(*string, sep='')


def main():
    string = input()
    solution(string)


if __name__ == '__main__':
    main()
