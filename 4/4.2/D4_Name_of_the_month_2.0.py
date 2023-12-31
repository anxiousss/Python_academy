def month(num, lang='ru'):
    num = str(num)
    d_ru = {"1": "Январь", "2": "Февраль", "3": "Март", "4": "Апрель", "5": "Май",
            "6": "Июнь", "7": "Июль", "8": "Август", "9": "Сентябрь", "10": "Октябрь",
            "11": "Ноябрь", "12": "Декабрь"}

    d_eng = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May",
             "6": "June", "7": "July", "8": "August", "9": "September", "10": "October",
             "11": "November", "12": "December"}

    if lang == 'ru':
        return d_ru[num]

    elif lang == 'en':
        return d_eng[num]


