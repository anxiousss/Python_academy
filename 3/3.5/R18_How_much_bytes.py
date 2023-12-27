import os


def solution(filename):

    with open(filename, 'rb') as fin:

        info = os.stat(filename)
        size = info.st_size

    if size < 1024:
        print(f'{size}Б')
    elif 1024 <= size <= 1024**2:
        print(f'{round(size // 1024) + 1}КБ')
    elif 1024**2 <= size <= 1024**3:
        print(f'{round(size // 1024**2) + 1}МБ')
    elif 1024**3 <= size <= 1024**4:
        print(f'{round(size // 1024**3) + 1}ГБ')


def main():
    filename = input()
    solution(filename)


if __name__ == '__main__':
    main()
