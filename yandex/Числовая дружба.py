all_ = []
for i in range(1, 10000):
    nums = []
    for j in range(1, i):
        if not i % j:
            nums.append(j)
    all_.append((i, sum(nums)))
check = []
ready = []
for i in all_:
    for j in all_:
        if i[0] == j[1] and i[1] == j[0] and i[0] != j[0]:
            now = [i[0], j[0]]
            now.sort()
            if now not in check:
                ready.append(now)
                check.append(now)
                break
ready.sort()
for i in ready:
    for j in i:
        print(j, end=' ')
    print()
