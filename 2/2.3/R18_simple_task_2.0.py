def solution(number):
    simple_mul = []
    i = 2
    while number != 1:
        if number % i == 0:
            simple_mul.append(i)
            number //= i
        else:
            i += 1

    print(*simple_mul, sep=" * ")


def main():
    number = int(input())
    solution(number)


if __name__ == '__main__':
    main()
