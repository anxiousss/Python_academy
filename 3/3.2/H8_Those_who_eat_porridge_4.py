def solution(N):

    names_and_porridges = {}
    right_guys = []
    for i in range(N):
        info = input().split()
        name, porridges = info[0], info[1:]
        names_and_porridges[name] = porridges

    what_we_want = input()
    for name, p in names_and_porridges.items():
        for porridge in p:
            if porridge == what_we_want:
                right_guys.append(name)

    right_guys.sort()

    if len(right_guys) != 0:
        print(*right_guys, sep='\n')
    else:
        print('Таких нет')


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
