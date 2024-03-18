def golden_ratio(i):
    list_ = [1, 1]
    for j in range(i - 1):
        list_.append(list_[-1] + list_[-2])
    print(list_[-1] / list_[-2])
