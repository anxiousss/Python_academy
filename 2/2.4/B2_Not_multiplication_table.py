def solution(Size):

    for i in range(1, Size + 1):
        for j in range(1, Size + 1):

            print(f"{j} * {i} = {i * j}")


def main():
    Size = int(input())
    solution(Size)


if __name__ == '__main__':
    main()
