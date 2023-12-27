def solution():
    all_strings = []
    while (string := input()) != "":
        all_strings.append(string.split())

    around = set()
    for string in all_strings:
        for s in string:
            if s == 'зайка':
                i = string.index(s)

                if string[i] != string[0]:
                    around.add(string[i - 1])

                if string[i] != string[-1]:
                    around.add(string[i + 1])

                string.remove(s)

    print(*around, sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
