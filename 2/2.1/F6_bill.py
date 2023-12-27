def solution(price, weight, cache, name):
    print("Чек")
    print(f"{name} - {weight}кг - {price}руб/кг")
    print(f"Итого: {price * weight}руб")
    print(f"Внесено: {cache}руб")
    print(f"Сдача: {int(cache - price * weight)}руб")


def main():
    name = input()
    price = int(input())
    weight = int(input())
    cache = int(input())
    solution(price, weight, cache, name)


if __name__ == "__main__":
    main()
