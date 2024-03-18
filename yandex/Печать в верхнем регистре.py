def print_upper(func):
    def new_print(*args):
        func(*map(lambda x: x.upper(), args))
    return new_print


print = print_upper(print)
