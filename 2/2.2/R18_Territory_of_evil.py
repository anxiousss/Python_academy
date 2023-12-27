def solution(a, b, c):
    max_side = max(a, b, c)
    min_side = min(a, b, c)
    left_side = (a + b + c) - min_side - max_side

    sum_of_squares_of_the_smaller_sides = min_side**2 + left_side**2

    if max_side**2 == sum_of_squares_of_the_smaller_sides:
        print("100%")

    elif max_side**2 < sum_of_squares_of_the_smaller_sides:
        print("крайне мала")

    else:
        print("велика")


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    solution(a, b, c)


if __name__ == '__main__':
    main()
