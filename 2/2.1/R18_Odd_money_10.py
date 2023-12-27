def solution(nominal, price):
    price = int(str(price), 2)
    print(nominal - price)


def main():
    price = int(input())
    nominal = int(input())
    solution(nominal, price)


if __name__ == '__main__':
    main()
    