def modern_print(string):
    if string not in strings:
        strings.add(string)
        print(string)


strings = set()
