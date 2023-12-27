def solution(start, end):

    for num in range(start, end + 1):
        print(num, end=' ')


def main():
    start = int(input())
    end = int(input())
    solution(start, end)


if __name__ == '__main__':
    main()
