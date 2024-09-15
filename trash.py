def print_goods(*args):
    lst = []
    for t in args:
        if type(t) == str:
            lst.append(t)
    for i, v in enumerate(lst):
        print(f"{i+1}. {v}")


print_goods(*list("abc"), 1, "hello")
