def linear(some_list):
    if len(some_list) == 0:
        return []
    elif not isinstance(some_list[0], list):
        return [some_list[0]] + linear(some_list[1:])
    else:
        return linear(some_list[0]) + linear(some_list[1:])
