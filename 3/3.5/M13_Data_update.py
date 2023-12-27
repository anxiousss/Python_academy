import json


def solution(filename):

    with open(filename, encoding='UTF-8') as fin:

        kv = json.load(fin)

    while True:
        try:
            string = input()
            string = string.split(' == ')
            key, value = string[0], string[1]
            kv[key] = value
        except EOFError:
            break

    with open(filename, 'w', encoding='UTF-8') as jf:
        json.dump(kv, jf, ensure_ascii=False, indent=2)


def main():
    filename = input()
    solution(filename)


if __name__ == '__main__':
    main()
