def solution(N):

    data = []
    namesakes = 0
    for i in range(N):

        name = input()
        data.append(name)

    for name in data:
        if data.count(name) > 1:
            namesakes += 1

    print(namesakes)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
