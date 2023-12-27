from sys import stdin

def solution():
    total = 0
    for line in stdin:

        numbers = line[:-1].split()

        for n in numbers:

            total += int(n)


    print(total)


def main():
    solution()


if __name__ == '__main__':
    main()
