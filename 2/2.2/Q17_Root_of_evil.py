def solution(a, b, c):

    D = b**2 - 4 * a * c

    if a == b == c == 0.0:
        print("Infinite solutions")

    elif a == b == 0.0:
        print("No solution")

    elif a == 0.0 and b != 0.0:
        print(f'{- c / b:.2f}')

    elif D > 0 and a != 0:
        root_1 = (- b + D**0.5) / (2 * a)
        root_2 = (- b - D**0.5) / (2 * a)

        if root_1 < root_2:
            print(f"{root_1:.2f} {root_2:.2f}")

        elif root_2 < root_1:
            print(f"{root_2:.2f} {root_1:.2f}")

    elif D == 0 and a != 0.0:
        print(f"{-b / (2 * a):.2f}")

    elif D < 0:
        print("No solution")


def main():
    a = float(input())
    b = float(input())
    c = float(input())
    solution(a, b, c)


if __name__ == '__main__':
    main()
