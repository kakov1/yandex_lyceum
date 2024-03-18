def rec_linear_sum(some_list):
    return rec_linear_sum(some_list[:-1]) + some_list[-1] if len(some_list) != 0 else 0
