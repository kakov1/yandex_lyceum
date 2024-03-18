def take_large_banknotes(banknotes):
    list_ = []
    for i in banknotes:
        if i > 10:
            list_.append(i)
    return list_
