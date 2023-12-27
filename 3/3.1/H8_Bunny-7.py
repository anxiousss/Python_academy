def solution(N):

    pos = 0
    for i in range(N):

        string = input()
        pos = string.find('зайка')

        if pos != -1:
            print(pos + 1)
        else:
            print('Заек нет =(')


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
