from requests import get


def main():

    server = 'http://' + input()
    key_name = input()

    req = get(server).json()

    print(req.setdefault(key_name) if req.setdefault(key_name) is not None else 'No data')


if __name__ == "__main__":
    main()
    
