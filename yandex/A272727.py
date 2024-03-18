list_, count = [], 0
for i in range(int(input())):
    print(count)
    list_ = list(list_)
    list_.append(count)
    count = 0
    count_1 = 0
    list_2 = list_
    list_ = tuple(list_)
    list_2.reverse()
    for j in list_:
        if j == list_2[count_1]:
            count += 1
        count_1 += 1
