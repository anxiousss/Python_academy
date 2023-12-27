def solution():

    while (string := str(input())) != '':

        if string[:2] == '##' and string[-3:] != '@@@':
            string = string.replace('##', '')
            print(string)

        elif string[:2] != '##' and string[-3:] != '@@@':
            print(string)


def main():
    solution()


if __name__ == '__main__':
    main()
