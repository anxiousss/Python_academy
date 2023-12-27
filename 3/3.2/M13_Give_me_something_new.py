def solution(N):

    all_dishes = []
    for i in range(N):
        dish = input()
        all_dishes.append(dish)

    M = int(input())
    cook_dishes = []

    for i in range(M):
        amount = int(input())

        for d in range(amount):
            cook_dish = input()
            cook_dishes.append(cook_dish)

    all_dishes = set(all_dishes)
    cook_dishes = set(cook_dishes)

    diff = all_dishes - cook_dishes
    if len(diff) > 0:
        diff = sorted(list(diff))
        print(*diff, sep='\n')
    else:
        print('Готовить нечего')


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
