def solution(filename):
    with open(filename, 'r', encoding='UTF-8') as fin:
        numbers = list(map(int, fin.read().split()))

        print(len(numbers))
        print(len([n for n in numbers if n > 0]))
        print(min(numbers))
        print(max(numbers))
        print(sum(numbers))
        print(f'{sum(numbers) / len(numbers):.2f}')


def main():
    filename = input()
    solution(filename)


if __name__ == '__main__':
    main()
