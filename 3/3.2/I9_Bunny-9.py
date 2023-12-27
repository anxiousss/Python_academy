def listmerge(lst):
    everything = []
    for lst in lst:
        everything.extend(lst)
    return everything


def solution():
    all_strings = []
    data = {}
    while (string := input()) != "":
        all_strings.append(string.split())

    all_strings_1 = listmerge(all_strings)
    for string in all_strings_1:
        data[string] = all_strings_1.count(string)

    for s, counts in data.items():
        print(s, counts)


def main():
    solution()


if __name__ == "__main__":
    main()
