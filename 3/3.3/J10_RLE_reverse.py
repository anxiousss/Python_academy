rle = [('a', 2), ('b', 3), ('c', 1)]

print(''.join(t[0] * t[1] for t in rle))