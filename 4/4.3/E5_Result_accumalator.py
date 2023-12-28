def result_accumulator(f):

    def decorated(*args, **kwargs):
        decorated.stack.append(f(*args))
        if kwargs.get('method') == 'drop':
            acc, decorated.stack = decorated.stack, []
            return acc

    decorated.stack = []
    return decorated


@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))
