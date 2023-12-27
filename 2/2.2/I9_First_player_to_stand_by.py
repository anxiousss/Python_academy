def solution(first_name, second_name, third_name):
    if first_name < second_name < third_name:
        print(first_name)

    elif first_name < third_name < second_name:
        print(first_name)

    elif second_name < first_name < third_name:
        print(second_name)

    elif second_name < third_name < first_name:
        print(second_name)

    elif third_name < first_name < second_name:
        print(third_name)

    else:
        print(third_name)


def main():
    first_name = input()
    second_name = input()
    third_name = input()
    solution(first_name, second_name, third_name)


if __name__ == '__main__':
    main()