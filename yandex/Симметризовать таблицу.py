height = int(input())
all_ = [input().split() for i in range(height - 1)]
count = 1
for i in range(height):
    i -= 1
    if i != -1:
        print(*all_[i], end=' ')
        print('0', end=' ')
        for j in all_[i + 1:]:
            print(j[i + 1], end=' ')
    else:
        print('0', end=' ')
        for j in all_:
            print(j[i + 1], end=' ')
    print()
    count += 1
