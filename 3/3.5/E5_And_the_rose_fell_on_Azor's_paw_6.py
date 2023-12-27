from sys import stdin


def is_palindrome(string):
    return string.lower() == string[::-1].lower()


def solution():

    lines = [line.rstrip("\n") for line in stdin]
    palindromes = set()
    for line in lines:
        line = line.split()

        for word in line:
            if is_palindrome(word.lower()):

                palindromes.add(word)

    palindromes = sorted(palindromes)
    print(*palindromes, sep='\n')


def main():
    solution()


if __name__ == '__main__':
    main()
