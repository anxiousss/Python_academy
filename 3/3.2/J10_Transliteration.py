def solution(string):
    russian_alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ,.:!?;'
    transliteration = {
        'А': 'A', 'Б': 'B', 'В': 'V',
        'Г': 'G', 'Д': 'D', 'Е': 'E',
        'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
        'И': 'I', 'Й': 'I', 'К': 'K',
        'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
        'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
        'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
        'Я': 'IA', 'Ь': '', 'Ъ': '',
        ',': ',', ' ': ' ', '!': '!',
        '.': '.', ':': ':', '*': '*',
    }

    new_string = string.upper()
    translate_string = ''

    for s1, s2 in zip(string, new_string):
        if s1 not in russian_alp:
            translate_string += s1
        if s1.isupper():
            translate_string += transliteration.get(s2).capitalize()
        else:
            translate_string += transliteration.get(s2).lower()

    print(translate_string)


def main():
    string = input()
    solution(string)


if __name__ == '__main__':
    main()
