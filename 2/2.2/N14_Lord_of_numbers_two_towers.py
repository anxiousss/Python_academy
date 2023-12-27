def solution(N):
    first_digit = N % 10
    second_digit = N // 10 % 10
    third_digit = N // 100

    max_digit = max(first_digit, second_digit, third_digit)
    min_digit = min(first_digit, second_digit, third_digit)
    left_digit = (first_digit + second_digit + third_digit) - min_digit - max_digit

    max_2_digit = int(str(max_digit) + str(left_digit))

    if min_digit == 0:
        min_2_digit = left_digit * 10

    else:
        min_2_digit = int(str(min_digit) + str(left_digit))

    print(min_2_digit, max_2_digit)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
    