def recursive_len(some_list):
    return 1 + recursive_len(some_list[:-1])\
        if ''.join(list(map(lambda x: str(x), some_list))) != '' else 0
