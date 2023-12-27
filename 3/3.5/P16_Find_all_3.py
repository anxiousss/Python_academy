from sys import stdin


def solution():
    lines = [line.rstrip("\n") for line in stdin]
    files = lines[1:]
    find = lines[0].lower().replace(' ', '')
    flag = False
    for file in files:

        with open(file, 'r', encoding='UTF-8') as fin:

            text = fin.read().replace(' ', '').replace('\t', '').replace('\n', '').strip(' ').lower()
            if find in text:
                flag = True
                print(file)

    if not flag:
        print('404. Not Found')


def main():
    solution()


if __name__ == '__main__':
    main()
