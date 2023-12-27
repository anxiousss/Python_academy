from sys import stdin


def solution():

    lines = [line.rstrip("\n") for line in stdin]
    req = lines[-1].lower()
    for i in range(len(lines) - 1):

        if req in lines[i].lower():
            print(lines[i])


def main():
    solution()


if __name__ == '__main__':
    main()
