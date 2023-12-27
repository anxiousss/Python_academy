def solution(N):
    if N < 2:
        return False

    for i in range(2, int(N**0.5 + 1)):
        if N % i == 0:
            return False
    else:
        return True


def main():
    N = int(input())
    ans = solution(N)

    if ans:
        print("YES")

    else:
        print("NO")


if __name__ == '__main__':
    main()
