def clear(filename1, filename2):

    with open(filename1, 'r', encoding='UTF-8') as fin1:

        text = ''
        for line in fin1.readlines():

            text += line.replace('\t', '').replace('\n', '').strip(' ') + '\n'

    with open(filename2, 'w', encoding='UTF-8') as fin2:

        new_text = ''
        for i in range(1, len(text)):

            if not text[i - 1].isspace():
                new_text += text[i - 1]
            elif text[i - 1] == ' ' and text[i] != ' ' != '\n':
                new_text += ' '

            elif text[i - 1] == '\n' and text[i] != '\n':
                new_text += '\n'

        fin2.write(new_text)

    print(new_text)


def main():
    filename1 = input()
    filename2 = input()
    clear(filename1, filename2)


if __name__ == '__main__':
    main()
