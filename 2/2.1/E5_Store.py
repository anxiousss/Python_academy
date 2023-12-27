def solution(price, weight, cache):
    print(int(cache - price * weight))


def main():
    price = int(input())
    weight = int(input())
    cache = int(input())
    solution(price, weight, cache)


if __name__ == "__main__":
    main()
