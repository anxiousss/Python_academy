def Is_palindrome(number):
    return number == number[::-1]


def solution(N):
    data = []

    for i in range(N):
        another_n = input()
        data.append(another_n)

    n_palindromes = 0
    for i in range(N):
        if Is_palindrome(data[i]):
            n_palindromes += 1

    print(n_palindromes)


def main():
    N = int(input())
    solution(N)


if __name__ == "__main__":
    main()
