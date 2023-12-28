from requests import delete


def main():

    server = 'http://' + input()
    id = int(input())
    delete(server + '/users/' + f'{id}')


if __name__ == '__main__':
    main()
