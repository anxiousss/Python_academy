def merge(left, right):
    try:
        iter(left)
        iter(right)
    except TypeError:
        raise StopIteration

    if (not (all(isinstance(i, type(left[0])) for i in left)
             and all(isinstance(i, type(left[0])) for i in right))):
        raise TypeError

    if list(left) != sorted(left) or list(right) != sorted(right):
        raise ValueError

    return tuple(sorted(list(left) + list(right)))
