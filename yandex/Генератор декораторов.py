def check_password(password):
    def decorator(func):
        print('Введите пароль:')
        entered = input()

        def decorated_func(*args, **kwargs):
            nonlocal password, entered
            if password != entered:
                print('В доступе отказано')
                return None
            else:
                return func(*args, **kwargs)
        return decorated_func
    return decorator
