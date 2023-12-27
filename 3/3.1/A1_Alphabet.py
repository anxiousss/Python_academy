def sol(N):
    for i in range(N):

        if (word := input())[0] not in 'абв':
            print('NO')
            break
    else:
        print('YES')


def main():
    N = int(input())
    sol(N)


if __name__ == '__main__':
    main()
