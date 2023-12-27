def solution(N):
    names = []
    for i in range(N):
        name = input()
        names.append(name)

    print(min(names), names)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
