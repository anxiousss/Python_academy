def solution(year):
    if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
        print("YES")

    else:
        print("NO")


def main():
    year = int(input())
    solution(year)


if __name__ == '__main__':
    main()
