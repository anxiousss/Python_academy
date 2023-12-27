def solution(a, b):
    div = a % b

    while div != 0:
        a = div
        div = b % div
        b = a

    return b


def main():
    data = list(map(int, input().split()))
    answer = data[0]
    for i in range(1, len(data)):
        answer = solution(answer, data[i])

    print(answer)


if __name__ == '__main__':
    main()
