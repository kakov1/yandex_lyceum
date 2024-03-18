def check_password(func):
    password = input()

    def decorated_func(*args, **kwargs):
        nonlocal password
        if password != 'password':
            print('В доступе отказано')
            return None
        else:
            return func(*args, **kwargs)
    return decorated_func


@check_password
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
