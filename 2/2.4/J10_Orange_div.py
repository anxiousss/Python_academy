def orange_division(n_slices):
    max_n_orange = n_sliсes - 2

    print("А Б В")
    for i in range(1, max_n_orange + 1):
        for j in range(1, max_n_orange + 1):
            for k in range(1, max_n_orange + 1):
                if i + j + k == n_sliсes:
                    print(f"{i} {j} {k}")


def main():
    n_slices = int(input())
    orange_division(n_sliсes)


if __name__ == "__main__":
    main()
