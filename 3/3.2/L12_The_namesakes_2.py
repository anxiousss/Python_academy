def solution(N):

    data = []
    counts = {}
    for i in range(N):

        name = input()
        data.append(name)

    data.sort()
    for name in data:
        if data.count(name) > 1:
            counts[name] = data.count(name)

    if counts == {}:
        print('Однофамильцев нет')

    else:
        for name, count in counts.items():
            print(f'{name} - {count}')


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
