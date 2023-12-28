def can_eat(horse_c, figure_c):
    x1, y1 = horse_c
    x2, y2 = figure_c

    if abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
        return True

    elif abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
        return True

    else:
        return False

