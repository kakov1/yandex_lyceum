def recursive_reverse(some_list):
    return [some_list[-1]] + recursive_reverse(some_list[:-1]) if some_list != [] else []
