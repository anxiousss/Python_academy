def solution():
    data = {}
    while (connection := input()) != '':
        connection = connection.split()
        if connection[0] not in data.keys():
            data[connection[0]] = {connection[1]}
        else:
            data[connection[0]].add(connection[1])

        if connection[1] not in data.keys():
            data[connection[1]] = {connection[0]}
        else:
            data[connection[1]].add(connection[0])

    new_data = {}
    for key in data.keys():
        new_data[key] = set()

    for i in data.keys():
        for j in data[i]:
            ans = data[j].copy()
            ans.discard(i)
            ans.difference_update(data[i])
            new_data[i] = new_data[i].union(ans)

    friends = sorted(new_data.items())
    for friend in friends:
        print(f'{friend[0]}: {", ".join(sorted(friend[1]))}')


def main():
    solution()


if __name__ == '__main__':
    main()
