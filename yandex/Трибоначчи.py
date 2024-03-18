def cached(func):
    cache = dict()

    def decorated_func(*args, **kwargs):
        if args[0] in cache.keys():
            result = cache[args[0]]
        else:
            result = cache[args[0]] = func(args[0])
        return result
    return decorated_func


@cached
def tribonacci(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
