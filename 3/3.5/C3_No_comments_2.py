from sys import stdin


def solution():

    lines = [line.rstrip("\n") for line in stdin]
    for line in lines:
        index = line.find('#')

        if '#' in line:

            if line[:index] == '' or line[:index] in ' ' or index == 0:
                continue
            else:
                print(line[:index].rstrip())

        elif index == -1:
            print(line)


def main():
    solution()


if __name__ == '__main__':
    main()
