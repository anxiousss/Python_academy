def solution(name, shalf_number):
    group_number = shalf_number // 100
    bed_number = shalf_number // 10 % 10
    child_number = shalf_number % 10
    print(f"Группа №{group_number}.")
    print(f"{child_number}. {name}.")
    print(f"Шкафчик: {shalf_number}.")
    print(f"Кроватка: {bed_number}.")


def main():
    name = input()
    shalf_number = int(input())
    solution(name, shalf_number)


if __name__ == "__main__":
    main()
