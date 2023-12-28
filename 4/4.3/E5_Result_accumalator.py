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
