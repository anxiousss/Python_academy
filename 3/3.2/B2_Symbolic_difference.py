def solution(set1, set2):
    set1 = set(set1)
    set2 = set(set2)
    print(*(set1 & set2), sep='')


def main():
    set1 = input()
    set2 = input()
    solution(set1, set2)


if __name__ == '__main__':
    main()
