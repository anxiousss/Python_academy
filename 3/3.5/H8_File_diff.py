def solution(filename1, filename2, filename3):

    with open(filename1, 'r', encoding='UTF-8') as fin1:

        words1 = set(list(fin1.read().split()))
    with open(filename2, 'r', encoding='UTF-8') as fin2:

        words2 = set(list(fin2.read().split()))

    with open(filename3, 'w', encoding='UTF-8') as fin3:

        no_rep = sorted(words1 ^ words2)

        for word in no_rep:
            print(word)
            fin3.write(word + '\n')


def main():
    filename1 = input()
    filename2 = input()
    filename3 = input()
    solution(filename1, filename2, filename3)


if __name__ == "__main__":
    main()
