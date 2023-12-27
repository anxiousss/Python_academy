def total(N):
    return sum(map(int, str(N)))


def solution(N):

    data = {}
    sums = []
    for i in range(N):
        child_name = input()
        child_number = int(input())

        sums.append(total(child_number))
        data[total(child_number)] = child_name

    max_total = max(sums)

    print(data.get(max_total))


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
