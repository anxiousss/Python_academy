from requests import get


def main():

    server = 'http://' + input() + '/users'
    information = get(server).json()

    users = []
    for user in information:

        name = ''
        for key, value in user.items():

            if key == 'last_name' or key == 'first_name':
                name += value + ' '

        users.append(name[:-1])

    print(*sorted(users), sep='\n')


if __name__ == '__main__':
    main()
