def solution(N):

    d_toys = {}
    # Создаём изначалный словарь, но т.к он кривой идём его исправлять
    for i in range(N):
        name, toys = input().split(': ')
        toys = toys.split(', ')
        for toy in toys:

            if toy not in d_toys:
                d_toys[toy] = []

            d_toys[toy].append(name)

    for toy, names in sorted(d_toys.items()):

        if len(set(names)) == 1:
            print(toy)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
