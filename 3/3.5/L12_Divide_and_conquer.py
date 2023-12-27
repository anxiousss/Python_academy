def count(number):

    evens = 0
    odds = 0
    for n in number:
        if int(n) % 2 == 0:
            evens += 1
        else:
            odds += 1

    if evens > odds:
        return 1
    elif evens < odds:
        return 2
    else:
        return 3


def solution(numbers_txt, even_txt, odd_txt, eq_txt):

    with open(numbers_txt, 'r', encoding='UTF-8') as nums:

        numbers = nums.readlines()

    with open(even_txt, 'w', encoding='UTF-8') as even:

        for number in numbers:
            for n in number.split():
                if count(n) == 1:
                    even.write(n)
                    even.write(' ')
            even.write('\n')

    with open(odd_txt, 'w', encoding='UTF-8') as odd:

        for number in numbers:
            for n in number.split():
                if count(n) == 2:
                    odd.write(n)
                    odd.write(' ')
            odd.write('\n')

    with open(eq_txt, 'w', encoding='UTF-8') as eq:

        for number in numbers:
            for n in number.split():
                if count(n) == 3:
                    eq.write(n)
                    eq.write(' ')

            eq.write('\n')


def main():
    numbers_txt = input()
    even_txt = input()
    odd_txt = input()
    eq_txt = input()
    solution(numbers_txt, even_txt, odd_txt, eq_txt)


if __name__ == '__main__':
    main()
