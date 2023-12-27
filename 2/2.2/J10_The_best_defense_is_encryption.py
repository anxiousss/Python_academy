def solution(password):
    first_sum = (password % 10) + (password // 10 % 10)
    second_sum = (password // 100) + (password // 10 % 10)

    if first_sum >= second_sum:
        crypt_password = str(first_sum) + str(second_sum)

    else:
        crypt_password = str(second_sum) + str(first_sum)

    print(crypt_password)


def main():
    password = int(input())
    solution(password)


if __name__ == '__main__':
    main()
    