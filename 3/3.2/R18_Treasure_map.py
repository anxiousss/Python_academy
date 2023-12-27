def find_of_treasures(N):

    coordinates = []
    for i in range(N):

        x, y = map(int, input().split())

        coordinates.append([x, y])

    coordinates.sort()

    n_max = {}
    for p in range(len(coordinates)):
        c = (coordinates[p][0] // 10, coordinates[p][1] // 10)

        if c not in n_max:
            n_max[c] = 0

        n_max[c] += 1

    print(max(n_max.values()))


def main():
    N = int(input())
    find_of_treasures(N)


if __name__ == '__main__':
    main()
