def convert(x, base):
    digits = []
    while x > 0:
        digits.append(x % base)
        x //= base

    return digits[::-1]


def total(N):
    return sum(map(int, str(N)))


def solution(N):
    numbers_and_sum = {}
    for i in range(2, 11):
        number_in_i = convert(N, i)
        sum_number_in_i = ''

        for n in number_in_i:
            sum_number_in_i += str(n)

        numbers_and_sum[i] = total(sum_number_in_i)

    max_b = float('-inf')
    a_accord_b = 0
    for i in numbers_and_sum.items():
        a, b = i

        if max_b < b:
            max_b = max(max_b, b)
            a_accord_b = a

    print(a_accord_b)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
