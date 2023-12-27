def solution(data, p):

    for n in data:
        print(n**p, end=' ')


def main():
    data = list(map(int, input().split()))
    p = int(input())
    solution(data, p)


if __name__ == '__main__':
    main()
