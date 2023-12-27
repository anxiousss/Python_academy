text = 'Мама мыла раму!'
print(sorted(text.lower()))
print({letter: text.lower().count(letter) for letter in sorted(text.lower()) if letter.isalpha()})
