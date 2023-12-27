def find_all(N):
    low_data = []
    upper_data = []
    for i in range(N + 1):
        page = input()
        low_page = page.lower()
        low_data.append(low_page)
        upper_data.append(page)

    req = low_data[-1]
    for i in range(N):
        if req in low_data[i]:
            print(upper_data[i])


def main():
    N = int(input())
    find_all(N)


if __name__ == "__main__":
    main()
