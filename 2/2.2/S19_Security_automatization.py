def solution(x, y):
    r_small = 5
    r_big = 10

    sphere_coordinates = (x ** 2 + y ** 2) ** 0.5
    parabola_coordinates = (0.25 * (x ** 2)) + (0.5 * x) + 8.75
    line_coordinates = ((5 * x) + 35) / 3

    if x >= 0 and y >= 0:

        if sphere_coordinates <= r_small:
            print("Опасность! Покиньте зону как можно скорее!")

        elif sphere_coordinates > r_big:
            print("Вы вышли в море и рискуете быть съеденным акулой!")

        else:
            print("Зона безопасна. Продолжайте работу.")

    elif x <= 0 <= y:

        if y <= 5 and y <= line_coordinates:
            print("Опасность! Покиньте зону как можно скорее!")

        elif sphere_coordinates > r_big:
            print("Вы вышли в море и рискуете быть съеденным акулой!")

        else:
            print("Зона безопасна. Продолжайте работу.")

    elif (x >= 0 >= y) or (x <= 0 and y <= 0):

        if y < parabola_coordinates:
            print("Опасность! Покиньте зону как можно скорее!")

        elif sphere_coordinates > r_big:
            print("Вы вышли в море и рискуете быть съеденным акулой!")

        else:
            print("Зона безопасна. Продолжайте работу.")

    elif x == 0 and y == 0:
        print("Опасность! Покиньте зону как можно скорее!")


def main():
    x = float(input())
    y = float(input())
    solution(x, y)


if __name__ == '__main__':
    main()
