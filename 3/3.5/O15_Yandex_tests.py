from sys import stdin
import json


def solution():
    results = [line.rstrip("\n") for line in stdin]
    all_points = 0
    flag = True
    with open('scoring.json', encoding='UTF-8') as scr:

        scores = json.load(scr)
        current_points = 0
        for el in scores:
            for key, value in el.items():
                if key == 'points':
                    current_points = value

                elif key == 'tests':
                    n_tests = len(value)
                    for test in value:

                        for data in test.items():
                            word, val = data
                            if word == 'pattern':
                                if val in results:
                                    all_points += current_points // n_tests

    print(all_points)


def main():
    solution()


if __name__ == '__main__':
    main()
