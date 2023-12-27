def morse_translation(string):
    string = string.upper()
    morse = {'A': '.- ', 'B': '-... ', 'C': '-.-. ',
             'D': '-.. ', 'E': '. ', 'F': '..-. ',
             'G': '--. ', 'H': '.... ', 'I': '.. ',
             'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
             'M': '-- ', 'N': '-. ', 'O': '--- ',
             'P': '.--. ', 'Q': '--.- ', 'R': '.-. ',
             'S': '... ', 'T': '- ', 'U': '..- ',
             'V': '...- ', 'W': '.-- ', 'X': '-..- ',
             'Y': '-.-- ', 'Z': '--.. ',
             '0': '----- ', '1': '.---- ', '2': '..--- ',
             '3': '...-- ', '4': '....- ', '5': '..... ',
             '6': '-.... ', '7': '--... ', '8': '---.. ',
             '9': '----. ', ' ': '\n'}
    translation_string = ''

    for s in string:
        translation_string += morse.get(s)

    print(translation_string)


def main():
    string = input()
    morse_translation(string)


if __name__ == '__main__':
    main()
