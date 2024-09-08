import functools


def candy_wrapper(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        s = fun(*args, **kwargs)
        print("------------------------")
        print(s)
        print("------------------------")
        return s

    return wrapper


@candy_wrapper
def ask(input):
    return input("Введите фразу: ")


ask(input)
