def print_format(first_name, second_name, third_name):
    print("{:^8}{:^8}{:^8}".format(" ", first_name, " "))
    print("{:^8}{:^8}{:^8}".format(second_name, " ", " "))
    print("{:^8}{:^8}{:^8}".format(" ", " ", third_name))
    print("{:^8}{:^8}{:^8}".format("II", "I", "III"))


def output(first_speed, second_speed, third_speed):

    if first_speed > second_speed > third_speed:
        print_format("Петя", "Вася", "Толя")

    elif first_speed > third_speed > second_speed:
        print_format("Петя", "Толя", "Вася")

    elif third_speed > second_speed > first_speed:
        print_format("Толя", "Вася", "Петя")
    elif third_speed > first_speed > second_speed:
        print_format("Толя", "Петя", "Вася")

    elif second_speed > third_speed > first_speed:
        print_format("Вася", "Толя", "Петя")

    else:
        print_format("Вася", "Петя", "Толя")



def solution(Petya_speed, Vasya_speed, Tolya_speed):

    output(Petya_speed, Vasya_speed, Tolya_speed)


def main():
    Petya_speed = int(input())
    Vasya_speed = int(input())
    Tolya_speed = int(input())
    solution(Petya_speed, Vasya_speed, Tolya_speed)


if __name__ == '__main__':
    main()
