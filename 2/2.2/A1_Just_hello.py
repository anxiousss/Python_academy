def solution(username, answer):
    print("Как Вас зовут?")
    print(f"Здравствуйте, {username}!")
    print("Как дела?")

    if answer == 'хорошо':
        print("Я за вас рада!")
    else:
        print("Всё наладится!")


def main():
    username = input()
    answer = input()
    solution(username, answer)


if __name__ == '__main__':
    main()