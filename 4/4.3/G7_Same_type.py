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
