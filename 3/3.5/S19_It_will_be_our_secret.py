from math import ceil


def crypt(shift):

    if abs(shift) > 26:
        shift = 26 - (26 * ceil(abs(shift) / 26) - abs(shift))

    if shift < -26:
        shift = 26 * ceil(abs(shift / 26)) - abs(shift)

    print(shift)
    alp = 'abcdefghijklmnopqrstuvwxyz' * 2
    lower_alp = [i for i in alp]
    capital_alp = [i for i in alp.upper()]

    with open('public.txt', 'r', encoding='UTF-8') as text:
        text = text.readlines()
    crypt_text = ''

    for word in text:
        for s in word:

            if s in lower_alp:
                low_index = lower_alp.index(s)
                crypt_text += lower_alp[low_index + shift]

            elif s in capital_alp:
                capital_index = capital_alp.index(s)
                crypt_text += capital_alp[capital_index + shift]

            else:
                crypt_text += s

    with open('private.txt', 'w', encoding='UTF-8') as prv:

        prv.write(crypt_text)


def main():
    shift = int(input())
    crypt(shift)


if __name__ == '__main__':
    main()
