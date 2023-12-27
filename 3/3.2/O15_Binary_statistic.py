def solution():

    numbers = list(map(int, input().split()))
    lst_of_dicts = []
    for n in numbers:
        data = {}
        n = bin(n)[2:]

        data["digits"] = len(n)
        data["units"] = n.count("1")
        data["zeros"] = n.count("0")
        lst_of_dicts.append(data)

    print(lst_of_dicts)


def main():
    solution()


if __name__ == "__main__":
    main()
