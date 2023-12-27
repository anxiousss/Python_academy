def solution(n1, n2):
    first_digit = (n1 // 100 + n2 // 100) % 10
    second_digit = (n1 // 10 % 10 + n2 // 10 % 10) % 10
    third_digit = (n1 % 10 + n2 % 10) % 10
    print(f'{first_digit}{second_digit}{third_digit}')


def main():
    n1 = int(input())
    n2 = int(input())
    solution(n1, n2)


if __name__ ==  '__main__':
    main()