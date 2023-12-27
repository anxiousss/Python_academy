def solution(Petya_speed, Vasya_speed):

    if Petya_speed > Vasya_speed:
        print("Петя")
    else:
        print("Вася")


def main():
    Petya_speed = int(input())
    Vasya_speed = int(input())
    solution(Petya_speed, Vasya_speed)


if __name__ == '__main__':
    main()