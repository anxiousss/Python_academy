def solution():
    left_border = 1
    right_border = 1000

    for i in range(10):
        center = (right_border + left_border) // 2
        print(center)
        answer = input()

        if answer == 'Меньше':
            right_border = center - 1

        elif answer == 'Больше':
            left_border = center + 1

        else:
            break


def main():
    solution()


if __name__ == '__main__':
    main()
