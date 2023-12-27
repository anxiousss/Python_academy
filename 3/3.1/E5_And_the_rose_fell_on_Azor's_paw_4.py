def solution(string):
    return string == string[::-1]


def main():
    string = input()

    if solution(string):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
