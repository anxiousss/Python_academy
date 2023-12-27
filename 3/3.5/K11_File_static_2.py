import json


def solution(txt_file, json_file):
    with open(txt_file, 'r', encoding='UTF-8') as txt:
        numbers = list(map(int, txt.read().split()))

        ln_all = len(numbers)
        ln_positive = len([n for n in numbers if n > 0])
        mn = min(numbers)
        mx = max(numbers)
        total = sum(numbers)
        mid = round(sum(numbers) / len(numbers), 2)

        stat = {"count": ln_all,
                "positive_count": ln_positive,
                "min": mn,
                "max": mx,
                "sum": total,
                "average": mid}

    with open(json_file, 'w', encoding='UTF-8') as jf:
        json.dump(stat, jf, ensure_ascii=False, indent='\t')


def main():
    txt_file = input()
    statistics_json = input()
    solution(txt_file, statistics_json)


if __name__ == '__main__':
    main()
