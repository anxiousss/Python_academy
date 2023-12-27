def no_comments():
    while (word := str(input())) != '':

        if '#' == word[0]:
            continue

        elif '#' in word and '#' != word[0]:
            del_pos = word.find('#')
            print(word[:del_pos])

        else:
            print(word)


def main():
    no_comments()


if __name__ == '__main__':
    main()
