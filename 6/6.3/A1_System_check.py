from requests import get


def main():
    req = get("http://127.0.0.1:5000").text
    print(req)


if __name__ == "__main__":
    main()
