def solution(number):
    without_even = ''
    while number > 0:

        if (number % 10) % 2 != 0:
            without_even = str(number % 10) + without_even

        number //= 10

    print(int(without_even))


def main():
    number = int(input())
    solution(number)


if __name__ == '__main__':
    main()
