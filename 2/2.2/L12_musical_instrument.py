def solution(side_a, side_b, side_c):

    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        print("YES")

    else:
        print("NO")


def main():
    side_a = int(input())
    side_b = int(input())
    side_c = int(input())
    solution(side_a, side_b, side_c)


if __name__ == '__main__':
    main()
