from requests import get
from sys import stdin


def main():
    server = "http://" + input() + "/users"
    id = int(input())
    server = server + f"/{id}"
    message = ''.join([line for line in stdin])

    information = get(server)
    if not information:
        print("Пользователь не найден")
        return

    information = information.json()
    if information and information['id'] == id:
        message = message.replace("{id}", str(id))
        for key in information.keys():

            if key != 'id':
                message = message.replace('{' + key + '}', information[key])

        print(message)


if __name__ == "__main__":
    main()
