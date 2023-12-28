from requests import get
from sys import stdin


def main():

    server = 'http://' + input()
    total = 0
    ways = [way.rstrip() for way in stdin]
    
    for way in ways:
        total += sum(get(server + way).json())

    print(total)


if __name__ == '__main__':
    main()
