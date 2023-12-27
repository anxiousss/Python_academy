def solution(number):
    origine = number
    reverse_number = 0

    while number > 0:
        reverse_number = reverse_number * 10 + number % 10
        number //= 10

    if reverse_number == origine:
        print("YES")
    else:
        print("NO")


def main():
    number = int(input())
    solution(number)


if __name__ == '__main__':
    main()
