from requests import get


def main():

    server = 'http://' + input()
    total = 0
    while data := int(get(server).text):
        total += data

    print(total)


if __name__ == '__main__':
    main()
