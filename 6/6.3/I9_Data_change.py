from requests import put
from sys import stdin


def main():
    server = 'http://' + input() + '/users'
    id = int(input())
    server = server + f'/{id}'
    changes = {line.rstrip('\n').split('=')[0]: line.rstrip('\n').split('=')[1] for line in stdin}

    put(server, json=changes)


if __name__ == '__main__':
    main()
