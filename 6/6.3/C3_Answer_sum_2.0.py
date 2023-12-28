from requests import get


def main():

    server = 'http://' + input()

    data = get(server).json()

    print(sum(el for el in data if type(el) is int))


if __name__ == '__main__':
    main()
