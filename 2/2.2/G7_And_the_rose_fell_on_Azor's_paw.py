def solution(N):
    first_digit = (N // 100 % 100) // 10
    second_digit = (N // 100 % 100) % 10
    third_digit = N // 10 % 10
    fourth_digit = N % 10

    if first_digit == fourth_digit and second_digit == third_digit:
        print("YES")

    else:
        print("NO")


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
    