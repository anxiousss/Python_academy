def unbox(lst):
    return ','.join(lst)


def solution(N):
    all_ingredients = []
    for i in range(N):
        ingredient = input()
        all_ingredients.append(ingredient)

    M = int(input())
    compare = {}
    big_dishes = []
    for i in range(M):
        big_dish = input()
        amount = int(input())
        big_dishes.append(big_dish)
        all_dishes = []

        for j in range(amount):
            dish = input()
            all_dishes.append(dish)
            compare[big_dish] = all_dishes

    flag = True
    answer_lst = []
    for d, i in compare.items():
        if len(i) > 1:
            for j in i:
                if j not in all_ingredients:
                    break
            else:
                flag = False
                answer_lst.append(d)

        i = unbox(i)
        if i in all_ingredients:
            flag = False
            answer_lst.append(d)

    if flag:
        print('Готовить нечего')

    answer_lst.sort()
    print(*answer_lst, sep='\n')


def main():
    N = int(input())
    solution(N)


if __name__ == "__main__":
    main()
