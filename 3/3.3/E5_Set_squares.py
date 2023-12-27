numbers = [1, 2, 3, 4, 5]
print(set([n for n in numbers if n**0.5 - round(n**0.5) == 0.0]))