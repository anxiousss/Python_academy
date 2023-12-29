class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):

    if not isinstance(a, int | float) and not isinstance(b, int | float) and not isinstance(c, int | float):
        raise TypeError

    D = b**2 - 4 * a * c

    if a == b == c == 0.0:
        raise InfiniteSolutionsError

    elif a == b == 0.0:
        raise NoSolutionsError

    elif a == 0.0 and b != 0.0:
        return -c / b, -c / b

    elif D > 0 and a != 0:
        root_1 = (- b + D**0.5) / (2 * a)
        root_2 = (- b - D**0.5) / (2 * a)

        if root_1 < root_2:
            return root_1, root_2

        elif root_2 < root_1:
            return root_2, root_1

    elif D == 0 and a != 0.0:
        return -b / (2 * a), -b / (2 * a)

    elif D < 0:
        raise NoSolutionsError
