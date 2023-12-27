def solution(Petya_speed, Vasya_speed, Tolya_speed):

    if (Petya_speed > Vasya_speed > Tolya_speed) or (Petya_speed > Tolya_speed > Vasya_speed):
        print("Петя")

    elif (Vasya_speed > Tolya_speed > Petya_speed) or (Vasya_speed > Petya_speed > Tolya_speed):
        print("Вася")

    else:
        print("Толя")


def main():
    Petya_speed = int(input())
    Vasya_speed = int(input())
    Tolya_speed = int(input())
    solution(Petya_speed, Vasya_speed, Tolya_speed)


if __name__ == '__main__':
    main()
