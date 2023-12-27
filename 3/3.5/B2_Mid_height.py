from sys import stdin


def solution():

    all_diff = 0
    c = 0
    for line in stdin:
        c += 1
        age, height1, height2 = line.split()

        diff = abs(int(height1) - int(height2))
        all_diff += diff

    print(round(all_diff / c))


def main():
    solution()


if __name__ == '__main__':
    main()
