def analysis():
    all_words = ''
    while (word := str(input())) != 'ФИНИШ':
        word = word.lower()
        all_words += word

    max_count = float("-inf")
    freq_letter = ''

    for letter in all_words:
        if letter == ' ':
            continue

        letter_count = all_words.count(letter)

        if max_count < letter_count:
            max_count = max(max_count, letter_count)
            freq_letter = letter

        elif max_count == letter_count:
            if freq_letter > letter:
                freq_letter = letter

    print(freq_letter)


def main():
    analysis()


if __name__ == '__main__':
    main()
