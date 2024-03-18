all_ = [input().split() for i in range(int(input()))]
dict_ = {}
count = 0
for i in all_:
    count_1 = 0
    for j in all_:
        if i == j:
            continue
        if i[count_1] == j[count_1]:
            all_[count].extend(j)
        count_1 += 1
    count += 1
print(all_)
