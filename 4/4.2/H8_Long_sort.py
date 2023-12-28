string = 'Яндекс использует Python во многих проектах'
print(sorted(string.split(), key=lambda el: (len(el), el.lower())))

