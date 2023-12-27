def solution(first_number, second_number):
    first_d_first_n = first_number // 10
    second_d_first_n = first_number % 10
    first_d_second_n = second_number // 10
    second_d_second_n = second_number % 10

    max_d = max(first_d_first_n, first_d_second_n, second_d_second_n, second_d_first_n)
    min_d = min(first_d_first_n, first_d_second_n, second_d_second_n, second_d_first_n)
    left_d = ((first_d_first_n + first_d_second_n + second_d_second_n + second_d_first_n) - max_d - min_d) % 10

    magic_number = int(str(max_d) + str(left_d) + str(min_d))

    print(magic_number)


def main():
    first_number = int(input())
    second_number = int(input())
    solution(first_number, second_number)


if __name__ == '__main__':
    main()
