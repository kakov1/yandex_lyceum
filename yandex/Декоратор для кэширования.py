def cached(func):
    cache = dict()

    def decorated_func(*args, **kwargs):
        if args[0] in cache.keys():
            result = cache[args[0]]
        else:
            result = cache[args[0]] = func(args[0])
        return result
    return decorated_func
