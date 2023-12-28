def same_type(f):
    def decorated(*args, **kwargs):

        first_arg = args[0]
        for i in range(1, len(args)):
            if type(first_arg) is not type(args[i]):
                print("Обнаружены различные типы данных")
                return None

        return f(*args)

    return decorated


@same_type
def combine_text(*words):
    return ' '.join(words)


print(combine_text('Hello,', 'world!') or 'Fail')
print(combine_text(2, '+', 2, '=', 4) or 'Fail')
print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')
