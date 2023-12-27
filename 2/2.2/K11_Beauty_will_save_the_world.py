def solution(N):
    first_digit = N % 10
    second_digit = N // 10 % 10
    third_digit = N // 100

    max_digit = max(first_digit, second_digit, third_digit)
    min_digit = min(first_digit, second_digit, third_digit)
    left_digit = (first_digit + second_digit + third_digit) - min_digit - max_digit

    if max_digit + min_digit == left_digit * 2:
        print("YES")

    else:
        print("NO")


def main():
    N = int(input())
    solution(N)


if __name__ == "__main__":
    main()
