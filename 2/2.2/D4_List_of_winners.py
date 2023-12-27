def solution(Petya_speed, Vasya_speed, Tolya_speed):
    if Petya_speed > Vasya_speed > Tolya_speed:
        print("1. Петя")
        print("2. Вася")
        print("3. Толя")

    elif Petya_speed > Tolya_speed > Vasya_speed:
        print("1. Петя")
        print("2. Толя")
        print("3. Вася")

    elif Vasya_speed > Tolya_speed > Petya_speed:
        print("1. Вася")
        print("2. Толя")
        print("3. Петя")

    elif Vasya_speed > Petya_speed > Tolya_speed:
        print("1. Вася")
        print("2. Петя")
        print("3. Толя")

    elif Tolya_speed > Vasya_speed > Petya_speed:
        print("1. Толя")
        print("2. Вася")
        print("3. Петя")

    else:
        print("1. Толя")
        print("2. Петя")
        print("3. Вася")


def main():
    Petya_speed = int(input())
    Vasya_speed = int(input())
    Tolya_speed = int(input())
    solution(Petya_speed, Vasya_speed, Tolya_speed)


if __name__ == '__main__':
    main()
    