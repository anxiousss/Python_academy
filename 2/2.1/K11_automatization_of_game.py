def solution(number):
    thousands = number // 100 % 10
    hundreds = number // 1000
    dozens = number % 10
    units = number // 10 % 10
    replaced_number = thousands * 1000 + hundreds * 100 + dozens * 10 + units
    print(replaced_number)


def main():
    number = int(input())
    solution(number)


if __name__ == "__main__":
    main()
