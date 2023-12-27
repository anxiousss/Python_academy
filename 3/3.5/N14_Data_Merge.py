import json


def solution(us, upd):
    users = {}
    for filename in [us, upd]:
        with open(filename, 'r', encoding='UTF-8') as fin:
            update = json.load(fin)

        for user in update:

            name = user['name']

            if name not in users:
                users[name] = {}

            info = users[name]
            for key, value in user.items():

                if key == 'name':
                    continue

                if key not in info:
                    info[key] = value
                else:
                    info[key] = max(info[key], value)

    with open(us, 'w', encoding='UTF-8') as us:
        json.dump(users, us, ensure_ascii=False, indent=4)

    print(users)


def main():
    users = input()
    updates = input()
    solution(users, updates)



if __name__ == '__main__':
    main()
