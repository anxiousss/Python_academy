def solution(string1, string2, string3):
    word = 'зайка'

    if word in string1 and word not in string2 and word not in string3:
        print(string1, len(string1))

    elif word in string2 and word not in string1 and word not in string3:
        print(string2, len(string2))

    elif word in string3 and word not in string1 and word not in string2:
        print(string3, len(string3))

    elif word in string1 and word in string2 and word not in string3:
        print(min(string1, string2), len(min(string1, string2)))

    elif word in string1 and word in string3 and word not in string2:
        print(min(string1, string3), len(min(string1, string3)))

    elif word in string2 and word in string3 and word not in string1:
        print(min(string2, string3), len(min(string2, string3)))

    else:
        print(min(string1, string2, string3), len(min(string1, string2, string3)))


def main():
    string1 = input()
    string2 = input()
    string3 = input()
    solution(string1, string2, string3)


if __name__ == '__main__':
    main()
