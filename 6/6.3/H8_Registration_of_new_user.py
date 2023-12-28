from requests import get, post


def main():

    server = 'http://' + input() + '/users'
    username = input()
    last_name = input()
    first_name = input()
    email = input()
    new_user = {'username': username, 'last_name': last_name, 'first_name': first_name, 'email': email}
    information = post(server, json=new_user)


if __name__ == '__main__':
    main()
