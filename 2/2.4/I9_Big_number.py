def max_digit(N):
    return max(map(int, str(N)))


def solution(N):

    max_number = ''
    max_numbers = []
    for i in range(N):
        child_number = int(input())

        max_numbers.append(max_digit(child_number))

    for i in range(N):
        max_number += str(max_numbers[i])

    print(max_number)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
