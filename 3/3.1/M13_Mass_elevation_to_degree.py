def solution(N):
    data = []
    for i in range(N):
        another_n = int(input())
        data.append(another_n)

    p = int(input())

    for n in data:
        print(n ** p)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()