all_ = [input() for i in range(int(input()))]
k = int(input())
for i in range(len(all_)):
    delete = []
    for j in range(len(all_)):
        if j == 0:
            delete.append(j)
        elif not j % k:
            delete.append(j)
    for j in range(len(delete)):
        print(all_[delete[j] - j])
        del all_[delete[j] - j]
